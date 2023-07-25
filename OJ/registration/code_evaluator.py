from OJ.settings import BASE_DIR
import docker
import os
import logging
from .models import TestCase, Result
import subprocess

def evaluate_code(submission):
    # Define the Docker client
    client = docker.from_env()

    # Define the Docker image based on the language
    if submission.language == 'python':
        image_name = 'python:3.8'
    elif submission.language == 'java':
        image_name = 'openjdk:8'
    else:
        # Handle unsupported languages here, if needed
        raise ValueError(f"Unsupported language: {submission.language}")

    try:
        # Pull the Docker image (if not already available)
        client.images.pull(image_name)

        # Create and start a new Docker container
        container = client.containers.run(image_name, detach=True)

        # Set up the file paths for code and test cases
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        code_path = os.path.join(BASE_DIR, 'judge_files', 'code_file')
        test_cases_path = os.path.join(BASE_DIR, 'judge_files', 'test_cases')

        # Retrieve test cases for the problem
        test_cases = TestCase.objects.filter(problem=submission.problem)

        # Create an empty list to store the results
        results = []
        total_passed = 0

        # # Start the Docker container
        # container.start()

        # # Check the container status
        # if container.status != 'running':
        #     # Handle container startup error here, if needed
        #     raise Exception("Container failed to start")

        # Iterate over the test cases
        for index, test_case in enumerate(test_cases, start=1):
            input_data = test_case.input_data.strip()
            expected_output = test_case.expected_output.strip()

            # Save the user's code to a temporary file
            code_file = os.path.join(test_cases_path, f'{submission.id}.py')
            with open(code_file, 'w') as f:
                f.write(submission.code)

            # Run the user's code using subprocess and capture the output
            process = subprocess.Popen(['python', code_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            try:
                stdout, stderr = process.communicate(input=input_data, timeout=5)
                output = stdout.strip()
                error = stderr.strip()
                # Check if the output matches the expected output
                is_passed = (output == expected_output)

                # Create a Result object for the current test case
                result = Result(
                    submission=submission,
                    test_case=test_case,
                    actual_output=output,
                    is_passed=is_passed
                )

                # Append the result to the list
                results.append(result)

                if is_passed:
                    total_passed += 1

            except subprocess.TimeoutExpired:
                # Handle time limit exceeded
                error = "Time Limit Exceeded"
                output = ""
                is_passed = False

            # Print the result for the current test case
            print(f"Test Case {index}: {'Accepted' if is_passed else 'Error'}")
            if not is_passed:
                print(f"Error: {error}")

        # Determine the overall verdict
        overall_verdict = all(result.is_passed for result in results)
        verdict = "Accepted" if overall_verdict else "Error"


        # Save the results to the database
        Result.objects.bulk_create(results)

        # Stop and remove the Docker container
        container.stop()
        container.remove()

        # Print the total number of test cases passed
        print(f"Total Test Cases Passed: {total_passed} / {len(test_cases)}")

        # Return the overall verdict
        return verdict

    except docker.errors.APIError as e:
        # Handle Docker APIError here, if needed
        raise
    except Exception as e:
        # Handle other exceptions here, if needed
        raise

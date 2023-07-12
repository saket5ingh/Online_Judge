from OJ.settings import BASE_DIR
import docker
import os
import logging
from .models import TestCase, Result

def evaluate_code(code, language):
    # Define the Docker client
    client = docker.from_env()

    # Define the Docker image based on the language
    if language == 'python':
        image_name = 'python:3.8'
    elif language == 'java':
        image_name = 'openjdk:8'

    try:
        # Pull the Docker image (if not already available)
        client.images.pull(image_name)

        # Create a new Docker container
        container = client.containers.create(image_name)

        # Set up the file paths for code and test cases
        code_path = os.path.join(BASE_DIR, 'judge_files', 'code_file')
        test_cases_path = os.path.join(BASE_DIR, 'judge_files', 'test_cases')

        # Retrieve test cases for the problem
        test_cases = TestCase.objects.all()

        # Create an empty list to store the results
        results = []

        # Start the Docker container
        container.start()

        # Check the container status
        if container.status != 'running':
            logging.error(f"Container {container.id} failed to start")
            raise Exception("Container failed to start")

        # Iterate over the test cases
        for test_case in test_cases:
            input_data = test_case.input_data.strip()
            expected_output = test_case.expected_output.strip()

            # Mount the code in the Docker container
            container_mounts = {
                code: {'bind': code_path, 'mode': 'ro'},
            }

            # Copy the code file to the Docker container
            container.exec_run(f'mkdir -p {code_path}')
            container.exec_run(f'echo "{code}" > {code_path}/code_file')

            # Run the code inside the Docker container
            cmd = f'python {code_path}' if language == 'python' else f'java {code_path}'
            exec_command = f"sh -c '{cmd}'"
            exit_code, output = container.exec_run(exec_command, stdin=input_data, stdout=True, stderr=True)

            # Decode the output from bytes to string
            output = output.decode().strip()

            # Decode the error from bytes to string
            error = output.decode().strip()

            # Create a Result object for the current test case
            result = Result(
                test_case=test_case,
                actual_output=output,
                is_passed=(output == expected_output.strip())
            )

            # Append the result to the list
            results.append(result)

        # Determine the overall verdict
        verdict = 'Accepted' if all(result.is_passed for result in results) else 'Wrong Answer'

        # Save the results to the database
        for result in results:
            result.save()

        # Stop and remove the Docker container
        container.stop()
        container.remove()

        # Return the overall verdict
        return verdict

    except docker.errors.APIError as e:
        logging.error(f"Docker APIError: {str(e)}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise

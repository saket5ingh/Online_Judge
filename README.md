
# Online Judge Platform

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Online Judge Platform is a web application that allows users to solve programming problems and evaluate their code submissions. It provides a platform for users to practice coding, improve their algorithmic skills.

This project is built using Django, a high-level Python web framework. It utilizes Docker for secure code execution and evaluation. The application provides a user-friendly interface for problem solving, code submission, and result evaluation.

## Features

- User registration and authentication
- Problem list page displaying problems available for solving
- Submission page for submitting code solutions to problems
- Evaluation of code submissions against test cases
- Verdict generation based on the evaluation results
- Admin panel for managing problems and submissions

## Technologies Used

- Django: A high-level Python web framework used for developing the backend of the online judge system.
- Docker: A containerization platform used to provide a secure and isolated environment for running code submissions.
- HTML, CSS, JavaScript: Frontend technologies used to create the user interface and enhance the user experience.
- PostgreSQL: A powerful open-source relational database used for storing user, problem, and submission data.

## Installation
1. Clone the repository:

```shell
git clone [https://github.com/your-username/online-judge-platform](https://github.com/saket5ingh/Online_Judge).git
cd online-judge-platform
```

2. Create and activate a virtual environment:
```shell
python3 -m venv env
source env/bin/activate
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Set up the database:
- Create a PostgreSQL database and update the database settings in `settings.py`.
- Run the database migrations:
  ```
  python manage.py migrate
  ```

5. Start the development server:
```
python manage.py runserver
```

6. Access the application in your browser at `http://localhost:8000`.

## Usage

- Register a new user account or log in with existing credentials.
- Browse the problem list to view available problems.
- Click on a problem to view the problem details.
- Submit your code solution for a problem through the submission page.
- View the verdict and results of your code submission.

## Contributing

Contributions to the Online Judge project are welcome! Here are some ways you can contribute:
- Submit bug reports or feature requests through the GitHub issues.
- Implement new features or enhancements and create a pull request.
- Help improve the documentation by suggesting clarifications or additions.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The Online Judge project was inspired by similar coding contest platforms and online judge systems.
- I would like to thank the Django, Docker, and PostgreSQL communities for their excellent tools and resources.
  
## Contact
If you have any questions or inquiries, please feel free to reach out to us:

Your Name: saketsingh9798@gmail.com
Project Repository: https://github.com/saket5ingh/Online_Judge


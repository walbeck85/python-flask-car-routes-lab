# Introduction to Flask – Car Routes Lab

---

## Overview

This repository contains my implementation of the **Introduction to Flask – Car Routes** lab. The goal of this lab is to demonstrate foundational Flask routing concepts by building a simple web application for a car company database. The application features routes that provide information about the company and specific car models.

---

## Features

- Initialization of a Flask application instance.
- Definition of a default route (`/`) that welcomes users to the company.
- Definition of a dynamic route (`/<model>`) that displays information about specific car models.
- Conditional route handling using an `existing_models` list to validate requested models.
- Testing of route responses using `pytest` to ensure correct functionality.

---

## Environment

- **Python Version:** 3.8.x
- **Operating System:** macOS
- **Dependency Management:** pipenv for virtual environment and package management

---

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/walbeck85/python-flask-car-routes-lab
   cd python-flask-car-routes-lab
   ```

2. **Install Dependencies**

   Run the following command to install required packages within a pipenv environment:

   ```bash
   pipenv install
   ```

3. **Activate the Virtual Environment**

   ```bash
   pipenv shell
   ```

4. **Run the Flask Application**

   Set the Flask app environment variable and start the development server:

   ```bash
   export FLASK_APP=app.py
   flask run
   ```

---

## File Structure

```
python-flask-car-routes-lab/
├── app.py
├── README.md
├── Pipfile
├── Pipfile.lock
├── tests/
│   └── test_app.py
└── __init__.py (if applicable)
```

---

## Running the Application

Once the Flask server is running, you can access the routes via a web browser or HTTP client:

- **Default Route:**  
  `http://127.0.0.1:5000/`  
  Returns: `"Welcome to Flatiron Cars"`

- **Model Route:**  
  `http://127.0.0.1:5000/Crossroads` (replace `Crossroads` with any model name)  
  Returns either:  
  - `"Flatiron Crossroads is in our fleet!"` if the model exists in `existing_models`  
  - `"No models called Crossroads exists in our catalog"` if it does not

---

## Testing

Run the test suite to verify that both routes behave as expected:

```bash
pytest -q
```

The tests validate:

- The default route (`/`) returns the correct welcome message.
- The model-specific route (`/<model>`) correctly identifies existing models and handles unknown models gracefully.

---

## Rubric Alignment

| Lab Requirement                            | Implementation Detail                            |
|-------------------------------------------|------------------------------------------------|
| Default route `/` returns welcome message | Implemented in `app.py` with route `/`          |
| Dynamic route `/<model>` returns model info | Implemented in `app.py` with conditional logic |
| Use of `existing_models` list              | Defined within `app.py` and used for validation |
| Testing with pytest                        | Tests located in `tests/test_app.py`             |

---

## Instructor Notes

To verify the lab completion:

- Run the Flask app as described.
- Access `/` and confirm the welcome message.
- Access `/<model>` with a model name from `existing_models` and verify the success message.
- Access `/<model>` with a non-existent model and confirm the error message.

---

## Branch and Pull Request Workflow

- Create a feature branch for development (e.g., `feature/car-routes`).
- Commit changes with descriptive messages.
- Push the feature branch to GitHub.
- Open a Pull Request targeting the `main` branch.
- After review, merge the PR into `main`.

---

## Troubleshooting

- **Flask Import Errors:** Ensure the pipenv shell is activated and Flask is installed (`pipenv install flask`).
- **Missing Packages:** Run `pipenv install` to install dependencies from the Pipfile.
- **Port Already in Use:** If `flask run` fails due to port conflicts, specify a different port using `flask run --port=5001`.
- **Environment Variables Not Set:** Make sure `FLASK_APP=app.py` is set before running the server. On Windows PowerShell, use `$env:FLASK_APP = "app.py"`.

---

Thank you for reviewing this lab submission.

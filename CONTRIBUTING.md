# Contributing to FastAPI Microservice

First off, thank you for considering contributing to our FastAPI Microservice! It's people like you that make this project such a great tool.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [How Can I Contribute?](#how-can-i-contribute)
4. [Style Guidelines](#style-guidelines)
5. [Commit Messages](#commit-messages)
6. [Pull Requests](#pull-requests)
7. [Development Setup](#development-setup)
8. [Running Tests](#running-tests)
9. [Documentation](#documentation)
10. [Community](#community)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to codewiththomppson@gmail.com.

## Getting Started

- Make sure you have a [GitHub account](https://github.com/signup/free)
- Submit a ticket for your issue, assuming one does not already exist.
  - Clearly describe the issue including steps to reproduce when it is a bug.
  - Make sure you fill in the earliest version that you know has the issue.
- Fork the repository on GitHub

## How Can I Contribute?

### Reporting Bugs

- Use a clear and descriptive title for the issue to identify the problem.
- Describe the exact steps which reproduce the problem in as many details as possible.
- Provide specific examples to demonstrate the steps.

### Suggesting Enhancements

- Use a clear and descriptive title for the issue to identify the suggestion.
- Provide a step-by-step description of the suggested enhancement in as many details as possible.
- Explain why this enhancement would be useful to most users.

### Your First Code Contribution

Unsure where to begin contributing? You can start by looking through these `beginner` and `help-wanted` issues:

- [Beginner issues](https://github.com/onlythompson/fastapi-microservice/labels/beginner) - issues which should only require a few lines of code, and a test or two.
- [Help wanted issues](https://github.com/onlythompson/fastapi-microservice/labels/help%20wanted) - issues which should be a bit more involved than `beginner` issues.

## Style Guidelines

### Python Style Guide

We follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code. Additionally:

- Use 4 spaces for indentation.
- Use type hints for function arguments and return values.
- Use docstrings for all public modules, functions, classes, and methods.

We use the following tools to enforce coding standards:

- `black` for code formatting
- `isort` for import sorting
- `flake8` for linting
- `mypy` for static type checking

Run these tools before submitting a pull request:

```bash
black .
isort .
flake8
mypy .
```

## Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

## Pull Requests

1. Update the README.md with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations, and container parameters.
2. Increase the version numbers in any examples files and the README.md to the new version that this Pull Request would represent.
3. You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

## Development Setup

1. Clone the repository:
   ```
   git clone https://github.com/onlythompson/fastapi-microservice.git
   cd fastapi-microservice
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up pre-commit hooks:
   ```
   pre-commit install
   ```

## Running Tests

To run the test suite, use the following command:

```bash
pytest
```

For test coverage, use:

```bash
pytest --cov=src tests/
```

## Documentation

- Keep README.md and other documentation up to date.
- Update the API documentation when you change or add new endpoints.
- Write clear, concise comments and docstrings.

## Community

- comming soon

Again, thank you for your contribution. We appreciate your effort and look forward to collaborating with you!
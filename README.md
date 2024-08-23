# FastAPI Microservice Template

Welcome to the FastAPI Microservice Template! This template provides a robust starting point for building scalable, maintainable, and efficient microservices using FastAPI, adhering to Clean Architecture principles and Domain-Driven Design (DDD).

## Table of Contents

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Generating the Project Structure](#generating-the-project-structure)
   - [Setting Up the Environment](#setting-up-the-environment)
4. [Documentation](#documentation)
5. [Contributing](#contributing)
6. [License](#license)

## Features

- Clean Architecture and Domain-Driven Design principles
- FastAPI for high-performance API development
- PostgreSQL database integration with SQLAlchemy ORM
- Redis for caching and distributed locking
- Kafka for asynchronous messaging
- Comprehensive testing setup (unit, integration, end-to-end)
- Kubernetes deployment configuration
- CI/CD pipeline setup (GitHub Actions and Jenkins)
- API documentation with Swagger/OpenAPI
- Logging and monitoring setup
- Security best practices implementation
- Scalability and performance optimizations

## Project Structure

```
my_fastapi_microservice/
├── src/
│   ├── application/
│   ├── domain/
│   │   └── events/
│   ├── infrastructure/
│   ├── presentation/
│   ├── core/
│   │   ├── feature_flags.py
│   │   ├── resilience.py
│   │   ├── secrets.py
│   │   └── rate_limiter.py
│   └── common/
├── tests/
│   └── performance/
│       └── locustfile.py
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
├── docs/
│   ├── api.md
│   ├── architecture.md
│   └── adr/
│       └── 0001-use-cqrs-pattern.md
├── ci/
│   ├── Jenkinsfile
│   └── github-actions-workflow.yml
├── scripts/
│   └── secret_rotation.sh
├── .env
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.8+
- Docker and Docker Compose
- Kubernetes cluster (for deployment)
- Git

### Generating the Project Structure

1. Clone this repository:
   ```
   git clone https://github.com/onlythompson/fastapi-microservice-template.git
   cd fastapi-microservice-template
   ```

2. Run the project structure generator script:
   ```
   python generate_project_structure.py my_fastapi_microservice
   ```

3. Navigate to your new project directory:
   ```
   cd my_fastapi_microservice
   ```

### Setting Up the Environment

1. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Copy the `.env.example` file to `.env` and update the environment variables:
   ```
   cp .env.example .env
   ```

4. Start the development server:
   ```
   uvicorn src.presentation.main:app --reload
   ```

Your FastAPI application should now be running at `http://localhost:8000`.


## Documentation

Comprehensive documentation for this project can be found in the `docs/` directory. Here are quick links to key documentation files:

- [API Documentation](docs/api.md): Detailed information about the API endpoints, request/response formats, and authentication.
- [Architecture Documentation](docs/architecture.md): Overview of the system architecture, including layers, design patterns, and key concepts.
- [Deployment Guide](docs/deployment.md): Instructions for deploying the microservice to various environments.
- [Development Guide](docs/development.md): Best practices and guidelines for developing and extending the microservice.
- [Testing Strategy](docs/testing.md): Overview of the testing approach, including unit, integration, and end-to-end testing.

### Architecture Decision Records (ADRs)

We use Architecture Decision Records (ADRs) to document important architectural decisions. You can find these in the `docs/adr/` directory:

- [ADR-0001: Use of CQRS Pattern](docs/adr/0001-use-cqrs-pattern.md)
- [ADR-0002: Choice of Database](docs/adr/0002-choice-of-database.md)
- [ADR-0003: API Versioning Strategy](docs/adr/0003-api-versioning-strategy.md)

For more detailed information about the architecture, API documentation, and development guidelines, please refer to the respective documents in the `docs/` directory.

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For more detailed information about the architecture, API documentation, and development guidelines, please refer to the documents in the `docs/` directory.

If you encounter any issues or have questions, please open an issue on the GitHub repository. Happy coding!
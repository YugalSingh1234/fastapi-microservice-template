# FastAPI Microservice Template

Welcome to the FastAPI Microservice Template! This template provides a robust starting point for building scalable, maintainable, and efficient microservices using FastAPI, adhering to Clean Architecture principles and Domain-Driven Design (DDD).

## Table of Contents

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Generating the Project Structure](#generating-the-project-structure)
   - [Setting Up the Environment](#setting-up-the-environment)
4. [Development Guidelines](#development-guidelines)
5. [Deployment](#deployment)
6. [Contributing](#contributing)
7. [License](#license)

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
   git clone https://github.com/yourusername/fastapi-microservice-template.git
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

## Development Guidelines

- Follow the principles of Clean Architecture and Domain-Driven Design.
- Write unit tests for all new features and maintain high test coverage.
- Use type hints throughout the codebase.
- Follow PEP 8 style guide for Python code.
- Document all public APIs using docstrings.
- Use feature flags for gradual rollouts and A/B testing.
- Implement proper error handling and logging.
- Use async/await for I/O-bound operations to improve performance.

## Deployment

This template includes Kubernetes manifests for deployment. To deploy your microservice:

1. Build and push your Docker image:
   ```
   docker build -t your-registry/my-fastapi-microservice:latest .
   docker push your-registry/my-fastapi-microservice:latest
   ```

2. Update the image in `k8s/deployment.yaml`.

3. Apply the Kubernetes manifests:
   ```
   kubectl apply -f k8s/
   ```

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For more detailed information about the architecture, API documentation, and development guidelines, please refer to the documents in the `docs/` directory.

If you encounter any issues or have questions, please open an issue on the GitHub repository. Happy coding!
# Architecture Documentation

## Table of Contents

1. [Overview](#overview)
2. [Architectural Principles](#architectural-principles)
3. [Project Structure](#project-structure)
4. [Layers](#layers)
   - [Domain Layer](#1-domain-layer-srcdomain)
   - [Application Layer](#2-application-layer-srcapplication)
   - [Infrastructure Layer](#3-infrastructure-layer-srcinfrastructure)
   - [Presentation Layer](#4-presentation-layer-srcpresentation)
   - [Core](#5-core-srccore)
   - [Common](#6-common-srccommon)
5. [Key Design Patterns and Concepts](#key-design-patterns-and-concepts)
6. [External Dependencies](#external-dependencies)
7. [Deployment Architecture](#deployment-architecture)
8. [Testing](#testing)
9. [Security Considerations](#security-considerations)
10. [Performance Optimizations](#performance-optimizations)
11. [Scalability](#scalability)
12. [Documentation](#documentation)
13. [Scripts](#scripts)
14. [Deadlock Management Strategy](#deadlock-management-strategy)
    - [Database Transaction Management](#1-database-transaction-management)
    - [Distributed Locking](#2-distributed-locking)
    - [Resource Ordering](#3-resource-ordering)
    - [Timeouts](#4-timeouts)
    - [Circuit Breaker Pattern](#5-circuit-breaker-pattern)
    - [Queue Management](#6-queue-management)
    - [Deadlock Detection](#7-deadlock-detection)
    - [Logging and Monitoring](#8-logging-and-monitoring)
    - [Testing](#9-testing)

## Overview

This document outlines the high-level architecture of our FastAPI Microservice. The architecture follows Clean Architecture principles and incorporates elements of Domain-Driven Design (DDD) to ensure a scalable, maintainable, and loosely coupled system.

## Architectural Principles

1. **Separation of Concerns:** The application is divided into distinct layers, each with a specific responsibility.
2. **Dependency Rule:** Dependencies point inwards. Inner layers are unaware of outer layers.
3. **Abstraction:** Use of interfaces and abstract classes to define boundaries between layers.
4. **Testability:** The architecture facilitates easy testing of business logic independent of external concerns.

## Project Structure

Our project follows this structure:

```
my_fastapi_microservice/
├── src/
│   ├── application/
│   │   ├── interfaces/
│   │   ├── services/
│   │   └── use_cases/
│   ├── domain/
│   │   ├── entities/
│   │   ├── value_objects/
│   │   └── events/
│   ├── infrastructure/
│   │   ├── database/
│   │   ├── repositories/
│   │   ├── messaging/
│   │   └── cache/
│   ├── presentation/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   └── schemas/
│   │   ├── grpc/
│   │   └── graphql/
│   ├── core/
│   │   ├── config.py
│   │   ├── exceptions.py
│   │   ├── logging.py
│   │   ├── events.py
│   │   ├── security.py
│   │   ├── middlewares.py
│   │   ├── telemetry.py
│   │   └── health.py
│   └── common/
│       ├── constants.py
│       └── utils.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docs/
├── scripts/
└── k8s/
```

## Layers

### 1. Domain Layer (`src/domain/`)

- **Responsibility:** Contains enterprise-wide business rules and entities.
- **Key Components:**
  - `entities/`: Core business entities
  - `value_objects/`: Immutable objects that are distinguishable only by their properties
  - `events/`: Domain events for important state changes
  - `exceptions.py`: Domain-specific exceptions

### 2. Application Layer (`src/application/`)

- **Responsibility:** Contains application-specific business rules and orchestrates the flow of data.
- **Key Components:**
  - `interfaces/`: Abstractions for repositories and services
  - `services/`: Application services implementing business logic
  - `use_cases/`: Use case implementations

### 3. Infrastructure Layer (`src/infrastructure/`)

- **Responsibility:** Contains implementations of interfaces defined in the application layer and all external concerns.
- **Key Components:**
  - `database/`: Database connection and configuration
  - `repositories/`: Implementations of repository interfaces
  - `messaging/`: Messaging implementations (e.g., Kafka)
  - `cache/`: Caching implementations (e.g., Redis)

### 4. Presentation Layer (`src/presentation/`)

- **Responsibility:** Handles external requests and responses.
- **Key Components:**
  - `api/`: FastAPI route definitions and request/response models
  - `grpc/`: gRPC service implementations (if applicable)
  - `graphql/`: GraphQL schema and resolvers (if applicable)

### 5. Core (`src/core/`)

- **Responsibility:** Contains cross-cutting concerns and shared utilities.
- **Key Components:**
  - `config.py`: Configuration management
  - `exceptions.py`: Global exception handling
  - `logging.py`: Logging configuration
  - `events.py`: Event handling
  - `security.py`: Security utilities
  - `middlewares.py`: Request/response processing middlewares
  - `telemetry.py`: Distributed tracing and monitoring
  - `health.py`: Health check endpoints

### 6. Common (`src/common/`)

- **Responsibility:** Shared utilities and constants used across the application.
- **Key Components:**
  - `constants.py`: Application-wide constants
  - `utils.py`: Shared utility functions

## Key Design Patterns and Concepts

1. **Repository Pattern:** Used in `src/infrastructure/repositories/` to abstract data persistence operations.
2. **CQRS (Command Query Responsibility Segregation):** Implemented in the application layer to separate read and write operations for complex domains.
3. **Event Sourcing:** Utilized in `src/domain/events/` for domains requiring a complete history of changes.
4. **Dependency Injection:** Used throughout the application, facilitated by FastAPI's dependency injection system.

## External Dependencies

1. **Database:** PostgreSQL for persistent storage, configured in `src/infrastructure/database/`.
2. **Caching:** Redis for distributed caching and locking, implemented in `src/infrastructure/cache/`.
3. **Messaging:** Apache Kafka for asynchronous communication, set up in `src/infrastructure/messaging/`.
4. **API Documentation:** Swagger/OpenAPI, automatically generated by FastAPI.

## Deployment Architecture

The microservice is designed to be deployed in a containerized environment, preferably on a Kubernetes cluster. Key components include:

1. **Dockerfile:** Located in the root directory for building the application container.
2. **docker-compose.yml:** In the root directory for local development and testing.
3. **Kubernetes Manifests:** Located in the `k8s/` directory, including:
   - `deployment.yaml`: For deploying the application
   - `service.yaml`: For internal networking
   - `ingress.yaml`: For external access

## Testing

The `tests/` directory is structured to support different types of tests:

- `unit/`: For testing individual components in isolation
- `integration/`: For testing interactions between components
- `e2e/`: For end-to-end testing of the entire system

## Security Considerations

Security measures are primarily implemented in `src/core/security.py` and include:

1. JWT-based authentication for API endpoints
2. Role-based access control (RBAC)
3. Integration with external secrets management (e.g., HashiCorp Vault)

## Performance Optimizations

1. Caching strategy using Redis, implemented in `src/infrastructure/cache/`
2. Database optimizations configured in `src/infrastructure/database/`
3. Asynchronous processing using background tasks and message queues

## Scalability

The architecture supports horizontal scalability through:

1. Stateless application design
2. Use of distributed caching (Redis)
3. Message-based communication (Kafka) for asynchronous processing
4. Database read replicas for scaling read operations



## Documentation

The `docs/` directory contains:

1. `api.md`: Detailed API documentation
2. `architecture.md`: This architecture overview
3. `adr/`: Architecture Decision Records for significant design decisions

## Scripts

The `scripts/` directory contains utility scripts for various tasks such as:

- `secret_rotation.sh`: For rotating secrets
- Other maintenance and deployment scripts


## Deadlock Management Strategy

To ensure the reliability and performance of our microservice, we've implemented a comprehensive deadlock management strategy. This strategy is crucial for preventing, detecting, and resolving potential deadlocks across various components of our system.

### 1. Database Transaction Management

- **Short-lived Transactions:** We use short-lived transactions to reduce the chance of conflicting locks.
- **Transaction Isolation Levels:** Appropriate isolation levels are set based on the specific requirements of each operation.
- **Implementation:** The strategy is implemented in `src/infrastructure/database/transaction.py`.

```python
# src/infrastructure/database/transaction.py
from contextlib import contextmanager

@contextmanager
def transaction_context(session):
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
```

### 2. Distributed Locking

- We use Redis for implementing distributed locks to manage shared resources across multiple instances of our service.
- The distributed locking mechanism is implemented in `src/infrastructure/cache/locks.py`.

```python
# src/infrastructure/cache/locks.py
class DistributedLock:
    def __init__(self, redis_client):
        self.redis_client = redis_client

    def acquire_lock(self, lock_name, timeout=10):
        return self.redis_client.lock(lock_name, timeout=timeout)

    def release_lock(self, lock):
        try:
            lock.release()
        except LockError:
            pass  # Lock was already released or expired
```

### 3. Resource Ordering

- We enforce a consistent order for acquiring resources across the application to prevent circular wait conditions.
- This ordering is maintained in the service layer (`src/application/services/`).

### 4. Timeouts

- All external calls and resource acquisitions are implemented with timeouts to prevent indefinite waiting.
- A utility for handling timeouts is provided in `src/common/timeout.py`.

```python
# src/common/timeout.py
import asyncio
from functools import wraps

def timeout(seconds):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            return await asyncio.wait_for(func(*args, **kwargs), timeout=seconds)
        return wrapper
    return decorator
```

### 5. Circuit Breaker Pattern

- We use the Circuit Breaker pattern to prevent cascading failures and provide fallback mechanisms.
- The implementation is in `src/core/circuit_breaker.py`.

```python
# src/core/circuit_breaker.py
class CircuitBreaker:
    def __init__(self, failure_threshold, recovery_timeout):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failures = 0
        self.last_failure_time = None
        self.state = "CLOSED"

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.state == "OPEN":
                if time.time() - self.last_failure_time > self.recovery_timeout:
                    self.state = "HALF-OPEN"
                else:
                    raise Exception("Circuit is OPEN")
            
            try:
                result = func(*args, **kwargs)
                if self.state == "HALF-OPEN":
                    self.state = "CLOSED"
                    self.failures = 0
                return result
            except Exception as e:
                self.failures += 1
                if self.failures >= self.failure_threshold:
                    self.state = "OPEN"
                    self.last_failure_time = time.time()
                raise e

        return wrapper
```

### 6. Queue Management

- Proper error handling and retries are implemented in message queue consumers to manage potential deadlocks in asynchronous processing.
- This is primarily handled in `src/infrastructure/messaging/kafka_consumer.py`.

### 7. Deadlock Detection

- We implement periodic checks for long-running transactions or locked resources.
- A background task runs at regular intervals to detect potential deadlock situations.

### 8. Logging and Monitoring

- Enhanced logging captures information about resource acquisition and release.
- We've implemented alerts for potential deadlock situations.
- These are configured in `src/core/logging.py` and `src/core/telemetry.py`.

### 9. Testing

- Specific tests for deadlock scenarios are included in the `tests/integration/` directory.
- We conduct chaos testing to simulate deadlock conditions in a controlled environment.

By implementing these strategies, we significantly reduce the risk of deadlocks in our system. This multi-faceted approach ensures that our microservice can handle concurrent operations efficiently and recover gracefully from potential deadlock situations.

This architecture provides a solid foundation for building scalable, maintainable, and performant microservices using FastAPI. It's designed to be flexible and can evolve as the project requirements grow and change over time.
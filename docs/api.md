# API Documentation

## Overview

This document provides a comprehensive guide to the APIs exposed by our FastAPI Microservice. It follows RESTful principles and uses JSON for request and response bodies.

## Base URL

All API endpoints are relative to the base URL:

```
https://api.example.com/v1
```

## Authentication

Most endpoints require authentication. Use Bearer token authentication by including an `Authorization` header in your requests:

```
Authorization: Bearer <your_access_token>
```

## Endpoints

### Users

#### Get User

Retrieves information about a specific user.

- **URL:** `/users/{user_id}`
- **Method:** GET
- **URL Params:** 
  - `user_id` (required): The ID of the user to retrieve
- **Success Response:**
  - Code: 200
  - Content: `{ "id": 123, "username": "johndoe", "email": "john@example.com" }`
- **Error Response:**
  - Code: 404
  - Content: `{ "detail": "User not found" }`

#### Create User

Creates a new user.

- **URL:** `/users`
- **Method:** POST
- **Data Params:** 
  ```json
  {
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "securepassword123"
  }
  ```
- **Success Response:**
  - Code: 201
  - Content: `{ "id": 124, "username": "newuser", "email": "newuser@example.com" }`
- **Error Response:**
  - Code: 400
  - Content: `{ "detail": "Username already exists" }`

### Items

#### Get Items

Retrieves a list of items.

- **URL:** `/items`
- **Method:** GET
- **Query Params:**
  - `page` (optional): Page number for pagination (default: 1)
  - `limit` (optional): Number of items per page (default: 20)
- **Success Response:**
  - Code: 200
  - Content: 
    ```json
    {
      "items": [
        { "id": 1, "name": "Item 1", "price": 19.99 },
        { "id": 2, "name": "Item 2", "price": 29.99 }
      ],
      "total": 50,
      "page": 1,
      "limit": 20
    }
    ```

## Error Handling

All endpoints may return the following error responses:

- 400 Bad Request: Invalid input data
- 401 Unauthorized: Missing or invalid authentication token
- 403 Forbidden: Insufficient permissions
- 404 Not Found: Requested resource not found
- 500 Internal Server Error: Unexpected server error

Error responses will include a JSON body with a `detail` field explaining the error.

## Rate Limiting

API requests are subject to rate limiting. The current limits are:

- 100 requests per minute for authenticated users
- 20 requests per minute for unauthenticated users

Rate limit information is included in the response headers:

- `X-RateLimit-Limit`: The number of allowed requests in the current period
- `X-RateLimit-Remaining`: The number of remaining requests in the current period
- `X-RateLimit-Reset`: The time at which the current rate limit window resets

## Versioning

The API is versioned using URL path versioning. The current version is `v1`. When breaking changes are introduced, a new version (e.g., `v2`) will be created, and the old version will be maintained for a deprecation period.

## Questions and Support

For questions or support regarding the API, please contact our developer support team at dev-support@example.com.
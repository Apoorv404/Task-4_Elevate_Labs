# Flask REST API

A simple RESTful API built with Flask that implements CRUD operations for managing users. This project was created as part of Task 4 for the Elevate Labs Internship.

## Features

- RESTful API endpoints for user management
- CRUD operations (Create, Read, Update, Delete)
- In-memory data storage
- JSON request/response format
- Error handling with appropriate HTTP status codes
- Simple and clean implementation

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone this repository
2. Install Flask:
   ```bash
   pip install flask
   ```

## How to Run

1. Start the Flask server:
   ```bash
   python app.py
   ```
2. The API will be available at `http://localhost:5000`

## API Endpoints

### GET /users
- Get all users or a specific user
- Query Parameters:
  - `id` (optional): Get a specific user by ID
- Response:
  - 200: Success
  - 404: User not found (when querying specific user)

### POST /users
- Add a new user
- Request Body:
  ```json
  {
    "id": "string",
    "name": "string",
    "age": number
  }
  ```
- Response:
  - 201: User created
  - 400: Invalid or existing user ID

### PUT /users/<user_id>
- Update an existing user
- Request Body:
  ```json
  {
    "name": "string",
    "age": number
  }
  ```
- Response:
  - 200: User updated
  - 404: User not found

### DELETE /users/<user_id>
- Delete a user
- Response:
  - 200: User deleted
  - 404: User not found

## Example Usage

### Add a User
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"id\":\"1\",\"name\":\"Apoorv\",\"age\":\"21\"}" http://127.0.0.1:5000/users
```

### Get All Users
```bash
curl http://localhost:5000/users
```

### Get Specific User
```bash
curl http://localhost:5000/users?id=1
```

### Update User
```bash
curl -X PUT http://localhost:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "John Smith", "age": 31}'
```

### Delete User
```bash
curl -X DELETE http://localhost:5000/users/1
```

## Project Structure

- `app.py`: Main application file containing the Flask API implementation
- `LICENSE`: Project license file
- `README.md`: This documentation file

## Technical Details

- Uses Flask's built-in development server
- Implements RESTful routing conventions
- Uses in-memory dictionary for data storage
- Includes proper error handling and status codes
- Debug mode enabled for development

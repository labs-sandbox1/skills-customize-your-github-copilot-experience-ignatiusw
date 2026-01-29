# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework. You'll create a RESTful web service with multiple endpoints, handle HTTP requests, work with JSON data, and implement basic CRUD operations.

## 📝 Tasks

### 🛠️ Create a Task Management API

#### Description
Build a REST API that manages a list of tasks. The API should support creating, reading, updating, and deleting tasks using HTTP methods (GET, POST, PUT, DELETE).

#### Requirements
Completed program should:

- Use FastAPI framework to create the web server
- Implement a GET endpoint to retrieve all tasks
- Implement a POST endpoint to create a new task
- Implement a PUT endpoint to update an existing task
- Implement a DELETE endpoint to remove a task
- Store tasks in memory (using a list or dictionary)
- Return proper HTTP status codes for each operation


### 🛠️ Add Data Validation

#### Description
Enhance your API with data validation to ensure tasks have required fields and proper data types. Use Pydantic models to define the task structure.

#### Requirements
Completed program should:

- Define a Pydantic model for Task with fields: id, title, description, and completed status
- Validate that title is required and non-empty
- Ensure id is an integer and completed is a boolean
- Return appropriate error messages for invalid data
- Include automatic API documentation at `/docs` endpoint

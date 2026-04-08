# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build efficient and modern REST APIs using the FastAPI web framework. You will create a fully functional API with proper request/response handling, data validation, and documentation.

## 📝 Tasks

### 🛠️ Create a Product Management API

#### Description
Build a REST API for managing a product catalog using FastAPI. Implement endpoints to create, retrieve, update, and delete products. Each product should have a name, description, price, and stock quantity.

#### Requirements
Completed program should:

- Create a Pydantic model for Product data validation
- Implement GET endpoint to retrieve all products
- Implement GET endpoint to retrieve a single product by ID
- Implement POST endpoint to create a new product
- Implement PUT endpoint to update an existing product
- Implement DELETE endpoint to remove a product
- Include proper error handling with appropriate HTTP status codes

### 🛠️ Add Query Parameters and Filtering

#### Description
Extend your API to support advanced filtering and searching capabilities. Allow users to filter products by price range, search by name, and apply sorting options.

#### Requirements
Completed program should:

- Implement query parameters for filtering by price range (min_price, max_price)
- Implement search functionality to filter products by name
- Implement sorting options (by price, by name, by stock)
- Return meaningful error messages when invalid filters are provided
- Ensure query parameters are optional with sensible defaults

### 🛠️ Test Your API

#### Description
Write test cases to verify your API endpoints work correctly. Test both successful operations and error scenarios.

#### Requirements
Completed program should:

- Test all CRUD operations for products
- Test query parameters and filtering logic
- Test error cases (invalid IDs, missing required fields, etc.)
- Achieve at least 80% code coverage for your API routes
- All tests should pass successfully

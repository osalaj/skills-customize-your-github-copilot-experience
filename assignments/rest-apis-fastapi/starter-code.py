"""
FastAPI REST API Starter Code - Product Management System

This starter code provides the basic structure for building a REST API
using FastAPI. Complete the TODO sections to implement the full functionality.
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

# Initialize FastAPI application
app = FastAPI(
    title="Product Management API",
    description="A REST API for managing products",
    version="1.0.0"
)

# TODO: Define Pydantic model for Product
# Create a model with fields: id (int), name (str), description (str), 
# price (float), and stock (int)
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int


# TODO: Define a Pydantic model for Product creation (without ID)
# This will be used for POST requests
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int


# In-memory database (for demonstration purposes)
products_db: List[Product] = [
    Product(id=1, name="Laptop", description="High-performance laptop", price=999.99, stock=5),
    Product(id=2, name="Mouse", description="Wireless mouse", price=29.99, stock=50),
    Product(id=3, name="Keyboard", description="Mechanical keyboard", price=79.99, stock=30),
]

next_id = 4


# TODO: Implement GET endpoint to retrieve all products
# Route: GET /products
# Optional query parameters: min_price, max_price, search, sort_by
@app.get("/products", response_model=List[Product])
def get_products(
    min_price: Optional[float] = Query(None, ge=0, description="Minimum price filter"),
    max_price: Optional[float] = Query(None, ge=0, description="Maximum price filter"),
    search: Optional[str] = Query(None, description="Search products by name"),
    sort_by: Optional[str] = Query("id", description="Sort by: id, name, price, or stock")
):
    """Get all products with optional filtering and sorting."""
    # Filter products
    filtered = products_db
    
    if min_price is not None:
        filtered = [p for p in filtered if p.price >= min_price]
    if max_price is not None:
        filtered = [p for p in filtered if p.price <= max_price]
    if search:
        filtered = [p for p in filtered if search.lower() in p.name.lower()]
    
    # Sort products
    if sort_by == "name":
        filtered.sort(key=lambda p: p.name)
    elif sort_by == "price":
        filtered.sort(key=lambda p: p.price)
    elif sort_by == "stock":
        filtered.sort(key=lambda p: p.stock)
    else:
        filtered.sort(key=lambda p: p.id)
    
    return filtered


# TODO: Implement GET endpoint to retrieve a single product by ID
# Route: GET /products/{product_id}
@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    """Get a specific product by ID."""
    for product in products_db:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


# TODO: Implement POST endpoint to create a new product
# Route: POST /products
@app.post("/products", response_model=Product, status_code=201)
def create_product(product: ProductCreate):
    """Create a new product."""
    global next_id
    new_product = Product(id=next_id, **product.dict())
    products_db.append(new_product)
    next_id += 1
    return new_product


# TODO: Implement PUT endpoint to update a product
# Route: PUT /products/{product_id}
@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product_update: ProductCreate):
    """Update an existing product."""
    for i, product in enumerate(products_db):
        if product.id == product_id:
            updated_product = Product(id=product_id, **product_update.dict())
            products_db[i] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")


# TODO: Implement DELETE endpoint to remove a product
# Route: DELETE /products/{product_id}
@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int):
    """Delete a product."""
    for i, product in enumerate(products_db):
        if product.id == product_id:
            products_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Product not found")


# Root endpoint
@app.get("/")
def read_root():
    """Welcome message."""
    return {
        "message": "Welcome to the Product Management API",
        "docs": "/docs"
    }


# To run this application:
# 1. Install FastAPI and Uvicorn: pip install fastapi uvicorn
# 2. Run the server: uvicorn starter-code:app --reload
# 3. Visit http://localhost:8000/docs to see the interactive API documentation

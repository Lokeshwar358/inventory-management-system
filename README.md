Inventory Management System

A command-line Inventory Management System built with Python to manage products using CRUD operations, JSON-based persistent storage, input validation, exception handling, modular programming, and automated testing with unittest.

Overview

This project was developed as a practical Python software engineering project. It started as a basic text-file inventory application and was progressively improved with modular functions, validation, error handling, JSON persistence, safer update/delete operations, and automated testing.

The application manages products containing:

Product ID

Product Name

Category

Price

Quantity

Features

Add new products

View all products

Search products by ID

Update product details

Delete products with confirmation

Calculate total inventory value

Generate low-stock reports

Prevent duplicate product IDs

Validate numeric and string input

Handle missing and invalid JSON files

Persist data using JSON

Automated testing with Python unittest

CRUD Operations

Create

Add a product with a unique ID, name, category, price, and quantity.

Read

View all products or search for a product by ID.

Update

Modify name, category, price, or quantity. Changes are first made on a temporary copy and are saved only after confirmation.

Delete

Remove a product after confirmation.

Inventory Features

Inventory Value

The total inventory value is calculated using:

Inventory Value = Price × Quantity

Low Stock Report

Products with quantity below 10 are considered low stock.

Quantity 9 → Low stock

Quantity 10 → Normal stock

Quantity 11 → Normal stock

Data Storage

The application uses JSON for persistent storage.

Example products.json:

[
    {
        "id": 101,
        "name": "Keyboard",
        "category": "Electronics",
        "price": 1200,
        "quantity": 10
    },
    {
        "id": 102,
        "name": "Mouse",
        "category": "Electronics",
        "price": 600,
        "quantity": 25
    }
]

Python's json.load() and json.dump() are used to read and write product data.

The application also handles:

Missing JSON files

Invalid JSON syntax

Invalid JSON structure

Validation and Exception Handling

The project validates:

Product ID must be greater than 0

Price must be greater than 0

Quantity must be 0 or greater

Product name cannot be empty

Category cannot be empty

Handled exceptions include:

ValueError

FileNotFoundError

JSONDecodeError

Project Structure

inventory-management-system/
│
├── inventory_management.py
├── test_inventory.py
├── products.json
├── test_products.json
└── README.md

inventory_management.py

Main application containing product management, validation, business logic, JSON persistence, and the command-line interface.

test_inventory.py

Automated test suite using Python's built-in unittest framework.

products.json

Actual inventory data.

test_products.json

Isolated data used by automated tests.

Technologies Used

Python 3

JSON

File Handling

Exception Handling

unittest

No external Python packages are required.

Python Concepts Demonstrated

Functions

Function arguments and return values

Lists

Dictionaries

Loops

Conditional statements

CRUD operations

Input validation

Exception handling

File handling

JSON serialization/deserialization

Modular programming

Separation of responsibilities

Dictionary copying

Automated testing

Test isolation

Application Menu

========================================
       INVENTORY MANAGEMENT SYSTEM
========================================

1. View Products
2. Add Product
3. Search Product
4. Update Product
5. Delete Product
6. Calculate Inventory Value
7. Low Stock Report
8. Exit

Automated Testing

The project includes automated tests covering core functionality and error conditions.

Current tests cover:

Finding an existing product

Handling a missing product

Loading products from JSON

Saving products

Updating products

Deleting products

Calculating total inventory value

Detecting low-stock products

Handling invalid JSON

Handling a missing JSON file

Run the tests with:

python test_inventory.py

Expected result:

..........
----------------------------------------------------------------------
Ran 10 tests

OK

Tests use separate test data so the application's real products.json is not modified during testing.

How to Run

Requirements

Python 3.x

Check the installed version:

python --version

Clone the repository

git clone https://github.com/YOUR_USERNAME/inventory-management-system.git
cd inventory-management-system

Run the application

python inventory_management.py

Run tests

python test_inventory.py

Development Approach

The project evolved through the following stages:

Basic Python CRUD
        ↓
Text-file persistence
        ↓
Input validation
        ↓
Exception handling
        ↓
Code refactoring
        ↓
Reusable functions
        ↓
JSON storage
        ↓
Business-logic separation
        ↓
Automated testing
        ↓
GitHub documentation

Future Improvements

Possible future improvements include:

SQLite database integration

Object-oriented architecture

Logging

REST API using Flask or FastAPI

Web interface

Authentication and authorization

Advanced inventory analytics

CSV import/export

Search, filtering, and sorting

Database transactions

Author

K. Lokeshwar Rao

GitHub: https://github.com/Lokeshwar358

License

This project was created for learning and portfolio purposes.

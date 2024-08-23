# Banking System

This Banking System is a robust and scalable application developed using FastAPI and MySQL. It provides essential functionalities for managing customer accounts, processing transactions, and ensuring data integrity. The application is built with a focus on security, reliability, and performance.
## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **MySQL**: A widely-used relational database management system for storing and managing banking data.
- **SQLAlchemy**: An ORM (Object-Relational Mapping) tool that simplifies database interactions.
- **Pydantic**: Utilized for data validation and serialization within FastAPI.
- **Uvicorn**: An ASGI web server implementation for serving the FastAPI application.
- **Python-dotenv**: Loads environment variables from a `.env` file.
- **Alembic**: A lightweight database migration tool for SQLAlchemy.

## Application Structure

The application is organized into the following modules:

### Components

- **main.py**:
  - The entry point of the application.
  - Defines the API endpoints for creating and managing customers, accounts, and transactions.
  - Utilizes FastAPI's dependency injection to manage database sessions.

- **models.py**:
  - Defines the SQLAlchemy models representing the database schema.
  - Includes `Customer`, `Account`, and `Transaction` models, each mapping to a corresponding table in the MySQL database.
  - Models define relationships, such as the one between `Customer` and `Account`.

- **schemas.py**:
  - Contains Pydantic models used for data validation and serialization.
  - Includes schemas for `Customer`, `Account`, and `Transaction`, with separate classes for creating and retrieving data.
  - Ensures that API requests and responses are correctly structured and validated.

- **crud.py**:
  - Implements the CRUD (Create, Read, Update, Delete) operations for interacting with the database.
  - Contains functions to create and retrieve customers, accounts, and transactions.
  - Handles business logic, such as updating account balances during transactions.

- **database.py**:
  - Manages the connection to the MySQL database using SQLAlchemy.
  - Sets up the database engine, session management, and base model class.
  - Loads environment variables, such as the database URL, from the `.env` file.


### Dependencies

- **requirements.txt**:
  - Lists all the Python packages required to run the application.
  - Includes FastAPI, Uvicorn, Pydantic, SQLAlchemy, MySQL client, Alembic, and Python-dotenv.

## Features

- **Customer Management**:
  - Create new customers with details like name, email, phone, address, and date of birth.
  - Retrieve customer information using their unique ID.

- **Account Management**:
  - Create accounts for customers, specifying account number and type (Savings or Checking).
  - Retrieve account details using the account ID.

- **Transaction Processing**:
  - Process deposits (Credit) and withdrawals (Debit) with automatic balance updates.
  - Ensure sufficient funds before processing withdrawals.

## How to Run the Project

### Prerequisites

- Ensure you have Python 3.7+ installed.
- Install MySQL and create a database for the project.

### Clone the Repository

```bash
git clone https://github.com/Gauri-03/banking-system.git
cd banking-system
```

### Set Up the Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up the MySQL Database

1. **Create a Database**:
   ```sql
   CREATE DATABASE banking_system;
   ```
2. **Update the `.env` File**:
   - Ensure the `DATABASE_URL` is correctly set in the `.env` file to point to your MySQL instance.

### Run the Application

```bash
uvicorn app.main:app --reload
```

### Access the API Documentation

- Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the Swagger UI for testing the API endpoints.

## Conclusion

This Banking System project is a comprehensive solution for managing banking operations, built with modern technologies like FastAPI and SQLAlchemy. It provides a secure and efficient platform for handling customer data, accounts, and transactions, making it a valuable tool for financial institutions.

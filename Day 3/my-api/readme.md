# Book Inventory API

## Overview
This is a lightweight REST API built with [FastAPI](https://fastapi.tiangolo.com/) that manages a book inventory. It connects to a local Microsoft SQL Server database using `pyodbc` to perform standard CRUD (Create, Read, Update, Delete) operations on book records.

---

## Prerequisites
Before running this application, ensure you have the following installed and configured on your system:

* **Python:** Version 3.7 or higher.
* **SQL Server:** A running instance of SQL Server Express (`localhost\SQLEXPRESS`).
* **ODBC Driver:** [ODBC Driver 17 for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server) installed on your machine.

---

## Database Configuration
The application expects a local SQL Server database named `BooksDB` with Windows Authentication (`Trusted_Connection=yes`). 

You must create a table named `Books` with the following schema for the API to function correctly:

```sql
CREATE DATABASE BooksDB;
GO

USE BooksDB;
GO

CREATE TABLE Books (
    Title NVARCHAR(255) PRIMARY KEY,
    Author NVARCHAR(255) NOT NULL,
    Available BIT NOT NULL
);
GO

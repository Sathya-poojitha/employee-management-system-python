# Employee Management System using Python & MySQL

## 📌 Project Overview

The Employee Management System is a menu-driven application developed using Python and MySQL. The system helps manage employee records efficiently by performing CRUD (Create, Read, Update, Delete) operations through a simple command-line interface.

This project demonstrates Python programming, database connectivity, SQL queries, and Object-Oriented Programming concepts.

---

## 🚀 Features

* Add Employee Records
* View Employee Records
* Search Employee by ID
* Update Employee Details
* Delete Employee Records
* MySQL Database Integration
* Menu-Driven Interface
* CRUD Operations

---

## 🛠️ Technologies Used

* Python
* MySQL
* MySQL Connector for Python
* SQL
* Object-Oriented Programming (OOP)

---

## 🗄️ Database Structure

### Database Name

```sql
employee_db
```

### Table Name

```sql
employees
```

### Table Fields

| Field Name | Data Type         |
| ---------- | ----------------- |
| emp_id     | INT (Primary Key) |
| emp_name   | VARCHAR(100)      |
| department | VARCHAR(50)       |
| salary     | DECIMAL(10,2)     |

---

## 📋 Functionalities

### 1. Add Employee

Allows users to add new employee records to the database.

### 2. View Employees

Displays all employee records stored in the database.

### 3. Search Employee

Searches employee details using Employee ID.

### 4. Update Employee

Updates employee information such as salary, department, or name.

### 5. Delete Employee

Removes employee records from the database.

---

## ▶️ How to Run the Project

### Step 1: Install Required Package

```bash
pip install mysql-connector-python
```

### Step 2: Create Database

```sql
CREATE DATABASE employee_db;
```

### Step 3: Create Employee Table

```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10,2)
);
```

### Step 4: Update Database Credentials

Modify the MySQL credentials in the Python file:

```python
host="localhost"
user="root"
password="your_password"
database="employee_db"
```

### Step 5: Run the Application

```bash
python employee_management_system.py
```

---

## 🎯 Learning Outcomes

* Python Programming
* Database Connectivity
* SQL Queries
* CRUD Operations
* Object-Oriented Programming
* Data Management
* Problem Solving

---

## 📈 Future Enhancements

* GUI using Tkinter
* Employee Login System
* Report Generation
* Data Export to Excel
* Web-Based Version using Flask

---

## 👩‍💻 Author

**Paluru Sathya Poojitha**

MCA Graduate | Python Developer | MySQL | SQL 

LinkedIn: https://linkedin.com/in/your-linkedin-profile

---

## ⭐ Conclusion

This project demonstrates the implementation of a complete Employee Management System using Python and MySQL. It provides hands-on experience in database integration, CRUD operations, and real-world application development, making it a valuable project for Python Developer roles.

import mysql.connector

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="employee_db"
)

cursor = conn.cursor()


# Add Employee
def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    emp_name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    query = """
    INSERT INTO employees
    (emp_id, emp_name, department, salary)
    VALUES (%s, %s, %s, %s)
    """

    values = (emp_id, emp_name, department, salary)

    cursor.execute(query, values)
    conn.commit()

    print("Employee Added Successfully")


# View Employees
def view_employees():
    cursor.execute("SELECT * FROM employees")

    records = cursor.fetchall()

    if records:
        print("\nEmployee Records")
        print("-" * 50)

        for row in records:
            print(row)
    else:
        print("No Records Found")


# Search Employee
def search_employee():
    emp_id = int(input("Enter Employee ID: "))

    query = "SELECT * FROM employees WHERE emp_id=%s"

    cursor.execute(query, (emp_id,))

    record = cursor.fetchone()

    if record:
        print("Employee Found:")
        print(record)
    else:
        print("Employee Not Found")


# Update Employee Salary
def update_employee():
    emp_id = int(input("Enter Employee ID: "))
    new_salary = float(input("Enter New Salary: "))

    query = """
    UPDATE employees
    SET salary=%s
    WHERE emp_id=%s
    """

    cursor.execute(query, (new_salary, emp_id))
    conn.commit()

    if cursor.rowcount > 0:
        print("Employee Updated Successfully")
    else:
        print("Employee Not Found")


# Delete Employee
def delete_employee():
    emp_id = int(input("Enter Employee ID to Delete: "))

    query = "DELETE FROM employees WHERE emp_id=%s"

    cursor.execute(query, (emp_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Employee Deleted Successfully")
    else:
        print("Employee Not Found")


# Main Menu
while True:

    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")

# Close Connection
conn.close()
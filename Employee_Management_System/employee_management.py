class Employee:

    def __init__(self, emp_id, name, department, salary):

        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary


employees = []

def save_to_file():

    with open("employees.txt", "w") as file:

        for emp in employees:

            file.write(
                f"{emp.emp_id},{emp.name},{emp.department},{emp.salary}\n"
            )

def load_from_file():

    try:

        with open("employees.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if len(data) == 4:

                    employee = Employee(
                        data[0],
                        data[1],
                        data[2],
                        data[3]
                    )

                    employees.append(employee)

    except FileNotFoundError:

        pass

def add_employee():

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")

    employee = Employee(emp_id, name, department, salary)

    employees.append(employee)
    
    save_to_file()
    
    print("Employee Added Successfully")


def view_employees():

    if len(employees) == 0:
        print("No Employees Found")
        return

    for emp in employees:

        print("---------------------")
        print("ID:", emp.emp_id)
        print("Name:", emp.name)
        print("Department:", emp.department)
        print("Salary:", emp.salary)


def search_employee():

    search_id = input("Enter Employee ID: ")

    for emp in employees:

        if emp.emp_id == search_id:

            print("Employee Found")
            print("ID:", emp.emp_id)
            print("Name:", emp.name)
            print("Department:", emp.department)
            print("Salary:", emp.salary)

            return

    print("Employee Not Found")


def delete_employee():

    delete_id = input("Enter Employee ID to Delete: ")

    for emp in employees:

        if emp.emp_id == delete_id:

            employees.remove(emp)

            print("Employee Deleted Successfully")

            return

    print("Employee Not Found")


def update_employee():

    update_id = input("Enter Employee ID: ")

    for emp in employees:

        if emp.emp_id == update_id:

            emp.name = input("Enter New Name: ")
            emp.department = input("Enter New Department: ")
            emp.salary = input("Enter New Salary: ")

            print("Employee Updated Successfully")

            return

    print("Employee Not Found")

load_from_file()

while True:

    print("\n===== Employee Management System =====")

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter Choice: ")

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
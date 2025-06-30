class Employee:
    salary_by_designation = {
        'Programmer': 25000,
        'Tester': 20000,
        'Manager': 30000
    }

    def __init__(self, name, age, designation):
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = Employee.salary_by_designation[designation]

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Designation: {self.designation}, Salary: {self.salary}"

    def raise_salary(self, amount):
        self.salary += amount

employees = {}

def create_employee():
    name = input("Enter employee name: ")
    if name in employees:
        print("Employee already exists!")
        return

    age_input = input("Enter employee age: ")
    if not age_input.isdigit():
        print("Invalid age input.")
        return
    age = int(age_input)

    print("Designations: Programmer, Tester, Manager")
    designation = input("Enter designation: ")
    designation = designation.capitalize()

    if designation not in Employee.salary_by_designation:
        print("Invalid designation.")
        return

    employee = Employee(name, age, designation)
    employees[name] = employee
    print("Employee added successfully.")

def display_employees():
    if not employees:
        print("No employees to display.")
    else:
        print("\nEmployee List:")
        for emp in employees.values():
            print(emp)

def raise_salary():
    name = input("Enter the name of the employee whose salary you want to raise: ")
    if name not in employees:
        print("Employee not found.")
        return

    amount_input = input("Enter amount to raise salary: ")
    if not amount_input.isdigit():
        print("Invalid amount.")
        return

    amount = int(amount_input)
    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    employees[name].raise_salary(amount)
    print(f"Salary raised for {name}. New salary: {employees[name].salary}")

def main():
    while True:
        print("\nMenu:")
        print("1. Create Employee")
        print("2. Display Employees")
        print("3. Raise Salary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            create_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            raise_salary()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

        cont = input("Do you want to continue? (Y/N): ")
        if cont.lower() != 'y':
            print("Thank you for using Employee Management System.")
            break

main()

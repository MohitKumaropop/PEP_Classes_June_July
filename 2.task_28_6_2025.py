class Employee:
    def __init__(self, name, age, designation):
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = self.set_initial_salary()

    def set_initial_salary(self):
        if self.designation.upper() == 'P':
            return 25000
        elif self.designation.upper() == 'M':
            return 30000
        elif self.designation.upper() == 'T':
            return 20000
        else:
            return 0

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Designation: {self.designation}")

    def raise_salary(self, percent):
        self.salary += self.salary * (percent / 100)
        print(f"New salary of {self.name} after {percent}% hike is: {self.salary}")


employees = []

while True:
    print("\n--- Employee Management System ---")
    print("1) Create Employee")
    print("2) Display Employees")
    print("3) Raise Salary")
    print("4) Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter your Name: ")
        age = int(input("Enter your Age (18-60): "))
        if age < 18 or age > 60:
            print("Invalid age! Please enter between 18 and 60.")
            continue

        print("Designation Options: P (25000), M (30000), T (20000)")
        designation = input("Enter your Designation (P/M/T): ")

        if designation.upper() not in ['P', 'M', 'T']:
            print("Invalid Designation! Choose P, M, or T.")
            continue

        emp = Employee(name, age, designation)
        employees.append(emp)
        print(f"Employee {name} added successfully!")

    elif choice == '2':
        if not employees:
            print("No employees to display.")
        else:
            print("\nEmployee List:")
            for emp in employees:
                emp.display()

    elif choice == '3':
        search_name = input("Enter the name of the employee: ")
        found = False
        for emp in employees:
            if emp.name.lower() == search_name.lower():
                percent_hike = float(input("Enter the percentage hike (e.g., 30 for 30%): "))
                emp.raise_salary(percent_hike)
                found = True
                break
        if not found:
            print(f"No employee found with the name: {search_name}")

    elif choice == '4':
        print("Thank you for using the application.")
        break

    else:
        print("Invalid choice! Please select from 1 to 4.")
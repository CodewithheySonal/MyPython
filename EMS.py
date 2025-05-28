# Employee Management Sysetem using OOP cooncepts:

# Let's create an Employee Class

class Employee:
    def __init__(self, name, employee_id, salary):  # Fixed order and typo
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        print(f"\nHello and Welcome to Employee Management System 😊")
        
    def get_details(self):
        print(f"\nEmployee Details:\nName: {self.name}\nEmployee ID: {self.employee_id}\nSalary: {self.salary:.2f}")

    def calculate_annual_salary(self):
        annual_salary = self.salary * 12
        print(f"\nAnnual Salary for {self.name} is: {annual_salary:.2f} Rupees")

class Manager(Employee):
    def __init__(self, department, employee_id, name, salary):
        super().__init__(name, employee_id, salary)  # Fixed order
        self.department = department
    
    def get_details(self):
        if self.employee_id <= "EMP005":
            print(f"\n{self.name}, your Manager of {self.department} is MK.")
        else:
            print(f"\n{self.name}, your Manager is yet to be assigned.")

class developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def get_details(self):
        print(f"\nHi {self.name}, you must have {self.programming_language} skill to proceed.")

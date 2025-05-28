# Main function to our EMS.py file for EMployee Management System

from EMS import *

emp1 = Employee("Sonal", "EMP001", 50000)
emp1.get_details()
emp1.calculate_annual_salary()

Manager_details_for_sonal = Manager("IT", "EMP001", "Sonal", 50000)
Manager_details_for_sonal.get_details()


developer_details_for_sonal = developer("Sonal", "EMP001", 50000, "Azure")
developer_details_for_sonal.get_details()

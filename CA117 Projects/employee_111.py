class Employee(object):
    
    NEXT_EMPLOYEE_NUMBER = 0
    
    def __init__(self, forename, surname, ssn, employee_number):
        self.forename = forename
        self.surname = surname
        self.ssn = ssn
        self.employee_number = employee_number
        self.NEXT_EMPLOYEE_NUMBER = employee_number + 1
    
    def __str__(self):
        pass
    
class SalariedEmployee(Employee):
    pass
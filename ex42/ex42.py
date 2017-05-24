class Employee:
    emp_count = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1
    
    def display_employee(self):
        print "Name: %s, Salary: %f" %(self.name, self.salary)
    
    def display_count(self):
        print "Total Number of Employees: %d" %Employee.emp_count

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
#inheritance and polymorphism
class Employee():
    def __init__(self, name, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary
        self.name = name
    def give_raise(self):
        self.salary = self.salary*1.05
    def reduc_sal(self):
        self.salary = self.salary/1.05
    def __repr__(self):
        return f'Employee Name: {self.name} \nEmployee ID: {self.emp_id} \nEmployee Salary: {self.salary}'
class Manager(Employee):
    def give_raise(self):
        self.salary = self.salary * 1.10

    def reduc_sal(self):
        self.salary = self.salary / 1.50
    def __repr__(self):
        return f'Manager Name: {self.name} \nManager ID: {self.emp_id} \nManager Salary: {self.salary}'
class Director(Employee):
    def give_raise(self):
        self.salary = self.salary * 1.20
    def __repr__(self):
        return f'Director Name: {self.name} \nDirector ID: {self.emp_id} \nDirector Salary: {self.salary}'


emp1 = Employee("Sophia", 101, 100000)
mgr1 = Manager("Kevwe", 202, 150000)
dri1 = Director("Lilian", 303, 200000)
print(type(emp1))
print(emp1.emp_id)
print(emp1.salary)
emp1.give_raise()
print(emp1.salary)
emp1.reduc_sal()
print(emp1.salary)
emp1.reduc_sal()
print(emp1.salary)
print(emp1)
print(type(mgr1))
print(mgr1)
mgr1.give_raise()
print("New salary after increase:",mgr1.salary)
mgr1.reduc_sal()
print("New salary after decrease:",mgr1.salary)

print(dri1)
print(type(dri1))
dri1.give_raise()
print("New salary after increase:", dri1.salary)
workers = [emp1,mgr1,dri1]
for emp in workers:
    print(emp)
    emp.give_raise()
for emp in workers:
    print(emp)

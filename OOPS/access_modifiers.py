# 04 - Public, Protected, and Private Attributes
# Python uses naming conventions rather than strict access modifiers.
#. == means public // ._ means protected // .__ private 
class Employee:
    def __init__(self, name, department, salary):
        self.name = name             # Public
        self._department = department  # Protected by convention
        self.__salary = salary       # Name-mangled (private-like)

    def show_details(self):
        print("Name:", self.name)
        print("Department:", self._department)
        print("Salary:", self.__salary)

employee = Employee("Mina", "Engineering", 50000)
employee.show_details()

# Public: normally accessed directly
print("\nPublic name:", employee.name)

# Protected: underscore means "internal use" by convention
print("Protected department:", employee._department)

# This direct access normally fails:
# print(employee.__salary)

# Python name-mangles double-underscore attributes.
# This form exists, but should not usually be used by outside code:
print("Name-mangled value:", employee._Employee__salary)

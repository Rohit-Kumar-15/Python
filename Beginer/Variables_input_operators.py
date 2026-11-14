#Variables, input, data types, and operators

name = input("What is your name? ")               #input
age = int(input("How old are you? "))

print("\nHello,", name)
print("Next year, you will be", age + 1)


course = "Python"
hours = 4.5
is_beginner = True

print("\nCourse:", course)  # /n - escape sequence
print("Study hours:", hours)
print("Beginner:", is_beginner)
print("Type of age:", type(age))  # type tell the data type 


a = 17
b = 5

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)  # without point 
print("Remainder:", a % b)
print("Power:", a ** b)    # power 
 
# String formatting
print(f"Hi {name}, welcome to {course}!")

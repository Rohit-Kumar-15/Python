# Functions, lists, tuples, dictionaries, and sets


def greet(name):
    print(f"Hello, {name}! Keep learning Python.")      # Function

greet("Alex")

def add(a, b):
    return a + b

print("Sum:", add(10, 20))


fruits = ["apple", "banana", "mango"]             # List
fruits.append("orange")
print("\nFruits:", fruits)
print("First fruit:", fruits[0])

for fruit in fruits:
    print(fruit)


coordinates = (10, 20)
print("\nCoordinates:", coordinates)         #Tuple

# Dictionary: key-value pairs
student = {
    "name": "Sam",
    "age": 20,
    "course": "Computer Science"
}
print("\nStudent name:", student["name"])
student["age"] = 21
print("Updated student:", student)


numbers = {1, 2, 2, 3, 4, 4}                     # Set
print("\nUnique numbers:", numbers)

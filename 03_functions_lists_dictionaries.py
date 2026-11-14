# FILE 3: Functions, lists, tuples, dictionaries, and sets


def greet(name):
    print(f"Hello, {name}! Keep learning Python.")      # Function

greet("Alex")

def add(a, b):
    return a + b

print("Sum:", add(10, 20))


fruits = ["apple", "banana", "mango"]             # List: ordered and changeable
fruits.append("orange")
print("\nFruits:", fruits)
print("First fruit:", fruits[0])

for fruit in fruits:
    print(fruit)


coordinates = (10, 20)
print("\nCoordinates:", coordinates)         # Tuple: ordered but cannot be changed

# Dictionary: key-value pairs
student = {
    "name": "Sam",
    "age": 20,
    "course": "Computer Science"
}
print("\nStudent name:", student["name"])
student["age"] = 21
print("Updated student:", student)

# Set: stores unique values
numbers = {1, 2, 2, 3, 4, 4}
print("\nUnique numbers:", numbers)

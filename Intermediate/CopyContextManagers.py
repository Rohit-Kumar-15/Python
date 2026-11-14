#Shallow Copy, Deep Copy, Context Managers

import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

deep = copy.deepcopy(original)

original[0].append(99)

print("Original:", original)
print("Shallow copy:", shallow)
print("Deep copy:", deep)

# Context manager

with open("context_demo.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python context managers!")
with open("context_demo.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("\nFile content:", content)

class SimpleContext:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        print("Leaving the context")
        return False  # Do not suppress exceptions

with SimpleContext():
    print("Inside the context")

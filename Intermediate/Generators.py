# 07 - Generators

def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1

for value in count_up_to(5):
    print(value)

squares = (number * number for number in range(1, 6))
print("Squares:", list(squares))

# Example: read a large file one line at a time
def read_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\n")


# Itertools - Infinite counters, combinations, permutations, grouping, product

import itertools

print("Count:", list(itertools.islice(itertools.count(10, 2), 5)))


print("Cycle:", list(itertools.islice(itertools.cycle(["A", "B"]), 6)))

print("Combinations:", list(itertools.combinations(["A", "B", "C"], 2)))


print("Permutations:", list(itertools.permutations(["A", "B", "C"], 2)))

print("Product:", list(itertools.product([1, 2], ["x", "y"])))


students = [
    {"name": "Asha", "grade": "A"},
    {"name": "Ravi", "grade": "B"},
    {"name": "Mina", "grade": "A"},
]
students.sort(key=lambda item: item["grade"])
for grade, group in itertools.groupby(students, key=lambda item: item["grade"]):
    print("Grade", grade, ":", [s["name"] for s in group])

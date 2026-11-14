# 02 - Itertools
# Infinite counters, combinations, permutations, grouping, product

import itertools

# count: generate an arithmetic sequence
print("Count:", list(itertools.islice(itertools.count(10, 2), 5)))

# cycle: repeat a sequence
print("Cycle:", list(itertools.islice(itertools.cycle(["A", "B"]), 6)))

# combinations: groups where order does not matter
print("Combinations:", list(itertools.combinations(["A", "B", "C"], 2)))

# permutations: arrangements where order matters
print("Permutations:", list(itertools.permutations(["A", "B", "C"], 2)))

# product: Cartesian product
print("Product:", list(itertools.product([1, 2], ["x", "y"])))

# groupby: group adjacent equal keys (sort first for global grouping)
students = [
    {"name": "Asha", "grade": "A"},
    {"name": "Ravi", "grade": "B"},
    {"name": "Mina", "grade": "A"},
]
students.sort(key=lambda item: item["grade"])
for grade, group in itertools.groupby(students, key=lambda item: item["grade"]):
    print("Grade", grade, ":", [s["name"] for s in group])

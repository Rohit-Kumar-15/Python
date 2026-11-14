# Itertools - Infinite counters, combinations, permutations, grouping, product
from itertools import combinations, permutations, product

print("Combinations:", list(combinations(["A", "B", "C"], 2)))


print("Permutations:", list(permutations(["A", "B", "C"], 2)))

print("Product:", list(product([1, 2], ["x", "y"])))

from itertools import accumulate
a = [1,2,3,4]
print (list(accumulate(a)))
print (list(accumulate(a, func=lambda x,y: x*y)))
print (list(accumulate(a, func=max)))

from itertools import groupby
def smallerthan3(x):
    return x < 3

print(lambda x: x<3)           #lambda expression

groupobj = groupby(a, key=smallerthan3)
for key,value in groupobj:
    print(key,list(value))

from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i ==15:
        break

b = [1,2,3]
for i in cycle(b):
    print(i)

for i in repeat(1, 4):
    print(i)

students = [
    {"name": "Asha", "grade": "A"},
    {"name": "Ravi", "grade": "B"},
    {"name": "Mina", "grade": "A"},
]
students.sort(key=lambda item: item["grade"])
for grade, group in groupby(students, key=lambda item: item["grade"]):
    print("Grade", grade, ":", [s["name"] for s in group])



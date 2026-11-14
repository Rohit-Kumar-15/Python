# Collections - Counter, namedtuple, defaultdict, deque

from collections import Counter

letters = "mississippi"
counts = Counter(letters)
print("Letter counts:", counts)
print("Most common:", counts.most_common(2))

from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "course"])
student = Student("Asha", 21, "CSE")

print("\nStudent:", student)
print("Name:", student.name)




from collections import defaultdict

marks = defaultdict(list)
marks["Asha"].append(92)
marks["Asha"].append(88)
marks["Ravi"].append(85)

print("\nMarks:", dict(marks))



from collections import deque


queue = deque(["task1", "task2"])
queue.append("task3")
queue.appendleft("urgent task")

print("\nQueue:", queue)
print("Processed:", queue.popleft())

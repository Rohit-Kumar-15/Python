# 01 - Python Collections
# Counter, namedtuple, defaultdict, deque

from collections import Counter, namedtuple, defaultdict, deque

# Counter: count how many times each item appears
letters = "mississippi"
counts = Counter(letters)
print("Letter counts:", counts)
print("Most common:", counts.most_common(2))

# namedtuple: tuple values with readable field names
Student = namedtuple("Student", ["name", "age", "course"])
student = Student("Asha", 21, "CSE")
print("\nStudent:", student)
print("Name:", student.name)

# defaultdict: automatically creates a default value for missing keys
marks = defaultdict(list)
marks["Asha"].append(92)
marks["Asha"].append(88)
marks["Ravi"].append(85)
print("\nMarks:", dict(marks))

# deque: efficient additions/removals at both ends
queue = deque(["task1", "task2"])
queue.append("task3")
queue.appendleft("urgent task")
print("\nQueue:", queue)
print("Processed:", queue.popleft())

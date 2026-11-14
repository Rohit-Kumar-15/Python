# FILE 2: if/elif/else, while loops, and for loops

# Check whether a number is positive, negative, or zero
number = int(input("Enter a number: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("The number is zero")

# Check whether a number is even or odd
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# for loop
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# while loop
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Go!")

# Simple password attempt example
secret = "python123"
attempt = ""

while attempt != secret:
    attempt = input("\nEnter the password: ")

print("Correct password!")

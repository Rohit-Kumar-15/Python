# if/elif/else, while loops, and for loops

number = int(input("Enter a number: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("The number is zero")



if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)


print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Go!")


secret = "python123"
attempt = ""

while attempt != secret:
    attempt = input("\nEnter the password: ")

print("Correct password!")

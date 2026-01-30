# Python program to swap two variables

# Take input from user
x = input("Enter value of x: ")
y = input("Enter value of y: ")

print(f"Before swapping: x = {x}, y = {y}")

# Swap using a temporary variable
temp = x
x = y
y = temp

print(f"After swapping: x = {x}, y = {y}")

# Basic Syntax, Conditional Statements and Loops - Lab
# 04_Number Between 1 and 100

number = float(input())

while number < 1 or number > 100:
    number = float(input())

print(f"The number {number} is between 1 and 100")

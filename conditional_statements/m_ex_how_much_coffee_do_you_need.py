# Basic Syntax, Conditional Statements and Loops - Lab
# More Exercises 05_How Much Coffee Do You Need

task = input()
coffee_needed = 0
task_list = "coding, dog, cat, movie"

while task != "END":

    if task in task_list.upper():
        coffee_needed += 2
    elif task in task_list.lower():
        coffee_needed += 1
    task = input()

if coffee_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_needed)


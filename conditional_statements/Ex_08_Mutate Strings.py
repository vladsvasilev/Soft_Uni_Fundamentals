# Basic Syntax, Conditional Statements and Loops - Lab
# Exercise 8

first_str = input()
second_str = input()

for i in range(len(first_str)):
    if first_str[i] != second_str[i]:
        replacement = second_str[i]
        new_str = first_str[0:i] + replacement + first_str[i +1:]

        first_str = new_str
        print(new_str)

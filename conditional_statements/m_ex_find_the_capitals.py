# Basic Syntax, Conditional Statements and Loops - Lab
# More Exercises 02_Find The Capitals

string = input()
capitals_list = []

for i in range(len(string)):
    if string[i].isupper():
        capitals_list.append(i)

print(capitals_list)

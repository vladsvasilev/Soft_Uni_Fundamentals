# Basic Syntax, Conditional Statements and Loops - Lab
# More Exercises 04_Sum of a Beach

string = input().lower()
count = 0
list = ['sand', 'water', 'fish', 'sun']

for word in list:
    if word in string:
        count += string.count(word)

print(count)

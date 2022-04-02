# Basic Syntax, Conditional Statements and Loops - Lab
# More Exercises 01_Find The Largest

number = input()
bigest_num = []
new_num = ""
for i in number:
    bigest_num.append(i)
bigest_num.sort(reverse=True)
for l in range(len(bigest_num)):
    new_num += bigest_num[l]

print(new_num)


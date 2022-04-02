# Basic Syntax, Conditional Statements and Loops - Lab
# More Exercises 03_Wolf in Sheep's Clothing

animals = input()

animals_list = []
sheep  = 0
animals_list = animals.split(", ")

for i in range(len(animals_list)):
    if i == len(animals_list) - 1 and animals_list[i] == "wolf":
        print('Please go away and stop eating my sheep')
        break
    elif animals_list[i] == "wolf":
        sheep = (len(animals_list) -1) - i
        print(f'Oi! Sheep number {sheep}! You are about to be eaten by a wolf!')
        break



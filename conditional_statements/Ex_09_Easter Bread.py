# Basic Syntax, Conditional Statements and Loops - Lab
# Exercise 9

budget = float(input())
price_flour = float(input())

price_of_egs = price_flour * 0.75
price_of_milk = price_flour * 1.25

money_left = budget
needed_flour = 1
needed_egs = 1
needed_milk = 0.25

number_of_breads = 0
colored_egs = 0

while budget != 0:
    money_left -= price_flour + price_of_egs + (price_of_milk * needed_milk)
    if money_left > 0:
        number_of_breads += 1
        colored_egs += 3
        budget = money_left
    else:
        break
    if number_of_breads % 3 == 0:
        colored_egs -= (number_of_breads -2)

print(f'You made {number_of_breads} loaves of Easter bread! Now you have {colored_egs} eggs and {budget:.2f}BGN left.')




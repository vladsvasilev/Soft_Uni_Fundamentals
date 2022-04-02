# Basic Syntax, Conditional Statements and Loops - Lab
# Exercise 6

number_of_orders = int(input())
total_sum = 0

for i in range(number_of_orders):
    price_capsule = float(input())
    days = int(input())
    capsule_count = int(input())

    order_sum = capsule_count * days * price_capsule
    total_sum += order_sum

    print(f'The price for the coffee is: ${order_sum:.2f}')

print(f'Total: ${total_sum:.2f}')
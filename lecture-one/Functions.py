"""

Functions
"""


def my_function():
    print("inside my functions")
my_function()

def print_my_name(first_name,last_name):
    print(f"Hello {first_name} {last_name} !")


print_my_name("saurabh","Kamble")


def buy_item(cost_of_item):
    return  cost_of_item + add_tax_to_item(cost_of_item)


def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    return cost_of_item * current_tax_rate


final_cost = buy_item(50)

print(final_cost)

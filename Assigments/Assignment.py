'''

Write a Python program that can do the following:

- You have $50

- You buy an item that is $15, that has a 3% tax

- Using the print()  Print how much money you have left, after purchasing the item.

'''
money =50
Tax =0.03
item = 15
purchasetax = item * Tax
totalspend = item + purchasetax

print(money - totalspend)

# Raw answer
print(50 -15 - (15 * 0.03))
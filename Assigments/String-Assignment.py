'''
String Assignment. (This can be tricky so feel free to watch solution so we can do it together)

- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days.
'''


days = int(input('How many days till your birthday ?'))
weeks = (round(days/7,2))
print(f" Hi {days} days and {weeks} week till birthday")
"""
Loops Assignment
Given: my_list = ["Monday", "Tuesday",
"Wednesday", "Thursday", "Friday"]
- Create a while loop that prints all
elements of the my_list variable 3 times.
- When printing the elements, use a for
loop to print the elements

"""

my_list = ["Monday", "Tuesday","Wednesday","Thursday","Friday"]


i = 0

while i < 3:
    i +=1
    print("==========")
    for x in my_list:
        if x == 'Monday':
           continue
        print(x)
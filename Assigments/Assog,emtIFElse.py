"""
If Else Assignment
- Create a variable grade holding an integer between 0 - 100
- Code if, elif, else statements to print the letter grade of
 the number grade variable

Grades:
A = 90 - 100
B = 80 - 89
C = 70-79
D = 60 - 69
F = 0 - 59
Example:

if grade = 87 then print('B')
"""

Grade = 55


if(Grade >= 90):
    print('A')
elif 80 <= Grade < 90:
    print('B')
elif 70 <= Grade < 80:
    print('C')
elif 60 <= Grade < 70:
    print('D')
else:
    print('F')
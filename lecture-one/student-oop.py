"""
Object Oriented Programming
"""


class Student:

    number_of_students =0
    school = "Online school"

    def __init__(self,first_name,last_name,major):
        self.first_name = first_name
        self.last_name = last_name
        self.major =major

        Student.number_of_students += 1

    def fullname_with_major(self):
        return f'{self.first_name}{self.last_name} is a '\
               f'{self.major} major !'

    def fullname_major_school(self):
        return f'{self.first_name} {self.last_name} is a '\
                f'{self.major} going to {self.school}'


    @classmethod
    def set_online_school(cls,new_school):
        cls.school = new_school

    @classmethod
    def split_students(cls,student_str):
        first_name,last_name,major = student_str.split('.')

        return cls(first_name,last_name,major)

student1 = Student('Saurabh','Kamble','Computer Science')
student2 = Student('Bhawgan','Kamble','Math')
new_student ='Adil.Yutzy.English'

student_3 = Student.split_students(new_student)
#student1.first_name = "saurabh"
#student1.last_name ="kamble"
#student1.major ="computer science"

#student2.first_name = "Bhagwan"
#student2.last_name ="kamble"
#student2.major ="Math"


Student.set_online_school('I use Google hangouts for class')
#print(student1.school)
#print(student2.school)
Student.set_online_school('I use Google hangouts for class !')
#print(student1.school)
#print(student2.school)
print(student_3.fullname_major_school())
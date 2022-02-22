"""
Object Oriented Programming- Inheritance !!
"""


class Student:

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greetings(self):
        return f'Hello ! I am {self.first_name} {self.last_name}'


class CollegeStudent(Student):
    def __init__(self,first_name,last_name,major):
        super().__init__(first_name,last_name)
        self.major = major

    def greetings(self):
        return f'{self.first_name} is a college student!'

class NonCollegeStudent(Student):
    def __init__(self,first_name,last_name,future_adult_job):
        super().__init__(first_name,last_name)
        self.future_adult_job =future_adult_job

    def grow_up(self):
        return f'When I grow up, I wan to be '\
               f'a {self.future_adult_job}'


student_1 = CollegeStudent('Saurabh','Kamble','Computer Science')
student_2 = NonCollegeStudent('John','Miller','Gamer')

print(student_1.greetings())
print(student_1.major)
print(student_2.greetings())
print(student_2.grow_up())


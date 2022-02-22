"""
Functions Assignment
- Create a function that takes in
3 parameters(firstname, lastname, age) and
returns a dictionary based on those values
"""



def userInformation_function(fist_name,last_name,age):
    user = {
        "name":fist_name,
        "surname":last_name,
        "age":age
    }

    return user




myvariable = userInformation_function(fist_name="saurabh",age="32",last_name="kamble")

print(myvariable)
"""
Dictionaries
"""


user_dictionary = {
    'username':'saurabh2836',
    'name':'saurabh kamble',
    'age':32

}

print(user_dictionary)
print(user_dictionary.get("username"))
print(user_dictionary.get("age"))

user_dictionary["married"] = False
print(user_dictionary)
print(len(user_dictionary))
print(user_dictionary)

for x in user_dictionary:
    print(x)

for x in user_dictionary.items():
    print(x)


user_dictionary2 = user_dictionary
print(user_dictionary);

user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop("age")
print(user_dictionary);
print(user_dictionary2);
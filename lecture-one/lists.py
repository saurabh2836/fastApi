'''
lists are a colleciton of data
'''


my_list =[80,96,72,100,8]

print(my_list[0])
print(my_list)

people_list = ["Eric","Saurabh","bhagwan"]

# Rewrite the list element with specific element
people_list[0] = "jayashri"
print(people_list)
# fetch last element
print(people_list[-1])
# length of the list
print(len(people_list))
# Specific element with reference to keys
print(people_list[0:2])
people_list.append("virat")
people_list.insert(2,"godfather")
print(people_list)
people_list.remove("Saurabh")
print(people_list)
people_list.pop(3)
print(people_list)
people_list.sort()
print(people_list)


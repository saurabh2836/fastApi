'''
Lists Assignment
- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals

'''


zoo = ['lion','deer','peacock','tiger','fox']
print(zoo)
zoo.pop(3)
zoo.append("Lizard")
zoo.pop(0)
print(zoo)
print(zoo[0:3])
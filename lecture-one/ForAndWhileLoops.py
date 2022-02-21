"""
For & While Loops
"""


#my_list = [1,2,3,4,5]

# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])

#sum_of_the_loop = 0
#for iterator in my_list:
   # sum_of_the_loop += iterator
#print(sum_of_the_loop)

#for x in range(1,3):
#   print(x)


#my_list = ["Monday","Tuesday","Wednesday","Saturaday"]


#for x in my_list:
 #   print(f"Happy {x} !")

i = 0

while i < 5:
    i +=1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("else loop")
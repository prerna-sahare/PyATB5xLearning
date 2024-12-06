my_list=[1,2,3]

print("element at the index 0- ", my_list[0])
print("element at the index 1- ", my_list[1])
print("element at the index 2- ", my_list[2])

my_list.append(4)
print(my_list)

my_list.append(5)
print(my_list)

my_list.extend([11,98,78])
print(my_list)

my_list.insert(6,"Oscar")
print(my_list)
print(len(my_list))

my_list[2]=("Nikhil")
print(my_list)

my_list.remove("Nikhil")
print(my_list)
print(len(my_list))
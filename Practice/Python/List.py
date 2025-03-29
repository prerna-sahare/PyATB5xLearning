my_List=[1,2,3]

print("element at the index 0-", my_List [0])
print("element at the index 1-", my_List [1])
print("element at the index 2-", my_List [2])

my_List.append(4)
print(my_List)

my_List.extend([5,6,7,8])
print(my_List)

my_List.insert(0,0)
print(my_List)

copy_my_List=my_List.copy()
print(my_List)
print(copy_my_List)
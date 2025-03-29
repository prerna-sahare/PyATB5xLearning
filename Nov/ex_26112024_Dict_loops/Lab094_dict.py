my_dict = {
    "name": "Prerna",
    "age": 32,
    "role": "sedt",
    "experiance":3,
}

print(my_dict["name"])

my_dict["role"]="tester"
print(my_dict)

del my_dict["age"]
print(my_dict)

for key, value in my_dict.items():
    print(key,"->", value)

# print("age"in my_dict)
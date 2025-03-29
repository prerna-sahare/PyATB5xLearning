my_dict={
    "name": "prerna",
    "age" :32,
    "role": "SDAT",
    "years": 30

}

print(my_dict["age"])

my_dict["age"]= 33

print(my_dict["age"])
print(my_dict)

for key, value in my_dict.items():
    print(key,"->", value)
student_infor={
    "name":"Nikhil",
    "age":34,
    "address": "AHM"

}

print(student_infor["age"])
print(student_infor["name"])
print(student_infor["address"])
print(student_infor)

for key,value in student_infor.items():
    print(key,"->",value)
print(student_infor)

student_infor2=dict(name="prerna",age=34,address="MH")
print(student_infor2)
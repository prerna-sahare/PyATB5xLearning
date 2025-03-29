student_infor1={
    "name":"Nikhil",
    "age":34,
    "address": {
        "home address": "AHM",
        "office address": "Local"
    }
}


student_infor2 = {
    "name": "Prerna",
    "age": 32,
    "address": {
        "home address": "Gondia",
        "office address": "moved"
    }

}
student_infor=[student_infor1, student_infor2]
print(student_infor)
print(student_infor[0])
print(student_infor[0]["name"])
print(student_infor[0]["address"])
print(student_infor[0]["address"]["office address"])
print(student_infor[1])
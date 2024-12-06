# create a program to sum of three number forom the user input
# if user doesnt enter any number, use default as 100, 200, 300
num1=int(input("enter num1 \n"))
num2=int(input("enter num2 \n"))
num3=int(input("enter num3 \n"))

def sum_of_three_num(num1=100, num2=200, num3=300):
    return num1+num2+num3

result=sum_of_three_num(num1,num2,num3)
print(result)

result2=sum_of_three_num()
print(result2)


# def say_hello(name="Prerna"):
#     print("Hello",name.upper())
#
# say_hello("Saahare")
#
#
# -----------------

num1=int(input("Enter Number1 \n"))
num2=int(input("Enter Number2 \n"))
num3=int(input("Enter Number3 \n"))

def sum_three_number(num1=100,num2=200,num3=300):
      return num1+num2+num3

result=sum_three_number(num1,num2,num3)

sum_three_number()
print(result)

result=sum_three_number()
print(result)
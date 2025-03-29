# def find_number(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
# find_number(8)

N1=int(input("Enter number \n"))
find_number = lambda num :"even" if num % 2 == 0 else "odd"
print(find_number(N1))

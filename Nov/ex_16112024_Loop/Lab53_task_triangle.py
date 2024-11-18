side1=int(input("enter value of side1\n"))
side2=int(input("enter value of side2\n"))
side3=int(input("enter value of side3\n"))
if side1==side2==side3:
    print("triangle is equilateral triangle")
elif side1==side3!=side2 or side3==side2!=side1 or side1==side2!=side3:
    print("triangle is isosceles triangle")
else:
    print("traingle is scalene triangle")
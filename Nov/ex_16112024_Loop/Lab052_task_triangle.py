angle1=int(input("enter the angle of triangle \n angle1"))
angle2=int(input("enter the angle of triangle \n angle2"))
angle3=int(input("enter the angle of triangle \n angle3"))
if angle1==angle2==angle3:
    print("the triangle is equlateral traingle")
elif angle1==angle2!=angle3:
    print("the traingle is iscosceles traingle")
elif angle1!=angle2==angle3:
    print("the traingle is iscosceles traingle")
elif angle1==angle3!=angle2:
    print("the traingle is iscosceles triangle")
else:
    print("the traingle is scalene triangle ")
year=int(input("Enter the Year\n"))
if year%4==0:
    print("this is Leap Year")
elif year%100==0 and year%400!=0:
    print("this is Leap Year")
else:
    print("THis is not leap yaer")
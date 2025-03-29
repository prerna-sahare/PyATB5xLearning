# for i in range(0,10):
#     if i ==5:
#         print("five")
#     else:
#         print(i)

# for i in range(0,10):
#     print(i)
#     if i ==5:
#         break


# write a program to ask the user which browser he want to run automation

browser_name=input("enter the browser name\n")
match browser_name:
    case"firefox":
        print("starting firefox")
    case"egde":
        print("Execute the egde code")
    case"chrome":
        print("Execute the chrome code")
    case "safari":
        print("Execute the safari code")
    case _:
        print("Browser not found!")
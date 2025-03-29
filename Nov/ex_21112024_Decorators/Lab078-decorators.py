
def add_security(func):

    def wrapper():
        print("before the function is called")
        print("add helmet,knee gaurd")
        func()
        print("after the function called")
        print("securedriving")

    return wrapper()





@add_security
def driving_scooty():
    print("normal function")
    print("I am driving scooty")


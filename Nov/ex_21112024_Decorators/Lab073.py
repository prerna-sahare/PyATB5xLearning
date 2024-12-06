
def add_extra_security(function):
    def wrapper():
        print("before running Tc")
        print("check the data")
        function()
        print("all test cases executed")
    return wrapper()


@add_extra_security
def test_ui():
    print("Im doing testing")
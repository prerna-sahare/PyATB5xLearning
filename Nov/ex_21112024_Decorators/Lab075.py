import time

def time_decorator(function):
    def wrapper():
        start_time=time.time()
        print(start_time)
        function()
        end_time=time.time()
        print(end_time)
        print("total time taken by function->", end_time-start_time)
    return wrapper()

@time_decorator
def test_ui_1():
    print("add a function, time taken by this function1")
    time.sleep(2)

@time_decorator
def test_ui_2():
    print("add a function, time taken by this function2")
    time.sleep(5)

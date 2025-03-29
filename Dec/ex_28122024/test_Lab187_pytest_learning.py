import pytest
import allure

def method1():
    print("Hello World")

@allure.title("methode2")
@pytest.mark.smoke
def method2():
    print("test1")
    assert 1+1==2

@allure.title("methode3")
@pytest.mark.regression
def methode3():
    print("tset2")
    assert 1-1==2
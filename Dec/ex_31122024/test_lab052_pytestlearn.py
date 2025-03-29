
import allure
import pytest
import requests

@allure.title("TC#1 - Verify that 2-2==0")
@allure.description("this is a basic math test")
@pytest.mark.smoke
def test_basic_math():
    assert 2-2 ==0


@allure.title("TC#2 - Verify that 3-3 is equal to 0")
@allure.description("this is a smoke testcase which check- verify that 3-3 is equal to 0")
@pytest.mark.regression
def test_sub1():
    assert 3-3 ==0


@allure.title("TC#2 - Verify that 1-1 is equal to 0")
@allure.description("this is a smoke testcase which check- verify that 1-1 is equal to 0")
@pytest.mark.smoke
def test_sub2():
    assert 1-1 ==0

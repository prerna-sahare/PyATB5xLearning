from selenium import webdriver
import allure
import pytest
import time


@allure.title("open the app.vwo.com")
@pytest.mark.regression
def test_vwo_login():
    driver=webdriver.edge()
    driver.get("https:/app.vwo.com")
    time.sleep(5)


def webdriver():
    return None
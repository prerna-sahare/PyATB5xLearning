
import allure
import pytest
import requests

@allure.title("TC#1- Create Booking CRUD Positive")
@allure.description("Verify the Create Booking!")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url= "https://restful-booker.herokuapp.com"
    base_path="/booking"

    full_url=base_url+base_path




@allure.title("TC#2- Create Booking CRUD Negative")
@allure.description("Verify that invalid payload Booking is not Created!")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    pass
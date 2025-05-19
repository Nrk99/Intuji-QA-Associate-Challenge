# from pages import user_Registration
import time
import pytest
from selenium.webdriver.chrome.options import Options
from pages.user_Registration import UserRegistration
from pages.singUp import Signup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.product import Product
from selenium import webdriver


@pytest.fixture
def setup():
    options = Options()
    prefs = {
        "credentials_enable_service": False,  # Disable credential service
        "profile.password_manager_enabled": False,  # Disable password manager
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--guest")
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automationexercise.com/login")
    yield driver
    driver.quit()


def test_user_registration(setup):
    registration_page = UserRegistration(setup)

    # Perform registration
    registration_page.setName("Ravi")
    registration_page.setEmail()
    registration_page.click_signUp()

    # def test_signup_registration(setup):
    signup_register = Signup(setup)
    signup_register.choose_gender()
    signup_register.set_password("zxcvvd@13")
    signup_register.set_days()
    signup_register.set_months()
    signup_register.set_years()
    signup_register.signup_checkbox()
    signup_register.receive_checkbox_check()
    signup_register.set_firstname("Krish")
    signup_register.set_lastname("rajan")
    signup_register.set_company("GLobal")
    signup_register.set_address1("Lalitpur")
    signup_register.set_address2("Patan")
    signup_register.set_state("Bagmati")
    signup_register.set_city("Kathmandu")
    signup_register.set_zipcode("00977")
    signup_register.set_mobilenumber("9851125556")
    signup_register.click_create_account()

    signup_register.is_user_logged_in()

    # def test_product(setup):
    prod = Product(setup)
    prod.click_product()
    prod.click_expand_women_dress()
    prod.click_dress()
    prod.click_view_product()
    prod.add_product_to_cart1()
    prod.click_polo()
    prod.click_view_product()
    prod.add_product_to_cart2()
    prod.click_product()
    prod.click_expand_women_dress()
    prod.click_dress()

    prod.verify_category_name()
    prod.click_view_product()
    prod.verify_product_name()
    prod.verify_product_price()
    prod.verify_stock_availability()
    prod.click_product()
    prod.choose_new_product_category()
    prod.click_view_product()
    prod.add_product_multiple_times(3)
    prod.delete_product()
    prod.procees_to_checkout()
    prod.verify_total_product_price()
    prod.click_place_order()
    prod.name_card()
    prod.enter_card_number()
    prod.enter_cvc()
    prod.enter_expiary_month()
    prod.enter_expiary_year()
    prod.pay_and_confirm_order()
    # time.sleep(20)

# import logging
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Signup:
    # after the registeration is created
    def __init__(self, driver):
        self.driver = driver

        # Find both radio buttons
        self.male_radio = (By.ID, "id_gender1")
        self.female_radio = (By.ID, "id_gender2")

        self.password = (By.ID, "password")
        self.days = (By.ID, "days")
        self.months = (By.ID, "months")
        self.years = (By.ID, "years")
        self.signUp_checkbox = (By.ID, "newsletter")
        self.receive_checkbox = (By.ID, "optin")
        self.first_name = (By.ID, "first_name")
        self.last_name = (By.ID, "last_name")
        self.company = (By.ID, "company")
        self.address1 = (By.ID, "address1")
        self.address2 = (By.ID, "address2")
        self.country_dropdown = (By.ID, "country")
        self.state = (By.ID, "state")
        self.city = (By.ID, "city")
        self.zipcode = (By.ID, "zipcode")
        self.mobileNumber = (By.ID, "mobile_number")
        self.create_account = (By.XPATH, "(//button[@type='submit'])[1]")

    def choose_gender(self):
        try:
            gender_locator = random.choice([self.male_radio, self.female_radio])
            gender_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(gender_locator)
            )
            gender_element.click()
        except Exception as e:
            print(f"Unexpected error while selecting gender: {e}")
            raise

    def set_password(self, password):
        try:
            password_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.password))
            )
            password_input.clear()
            password_input.send_keys(password)
        except Exception as e:
            print("failed to enter the password!")

    def set_days(self):
        try:
            days_input = Select(
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((self.days))
                )
            )
            days_input.select_by_value("14")
        except Exception as e:
            print("Failed to set days!")

    def set_months(self):
        try:
            months_input = Select(
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((self.months))
                )
            )
            months_input.select_by_value("5")
        except Exception as e:
            print("failed to set months!")

    def set_years(self):
        try:
            years_input = Select(
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((self.years))
                )
            )
            years_input.select_by_value("2000")
        except Exception as e:
            print("fialed to set years!")

    def signup_checkbox(self):
        try:
            checkbox = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((self.signUp_checkbox))
            )
            checkbox.click()
        except Exception as e:
            print("failed to sign up checkup!")

    def receive_checkbox_check(self):
        try:
            checkbox = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((self.receive_checkbox))
            )
            checkbox.click()
        except Exception as e:
            print("Failed to receciver checkbox!")

    def set_firstname(self, first_name):
        try:
            firstname_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.first_name))
            )
            firstname_input.clear()
            firstname_input.send_keys(first_name)
        except Exception as e:
            print("failed to set first name!")

    def set_lastname(self, last_name):
        try:
            lastname_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.last_name))
            )
            lastname_input.clear()
            lastname_input.send_keys(last_name)
        except Exception as e:
            print("failed to enter last name!")

    def set_company(self, company):
        try:
            company_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.company))
            )
            company_input.send_keys(company)
        except Exception as e:
            print("failed to set company!")

    def set_address1(self, address1):
        try:
            address1_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.address1))
            )
            address1_input.clear()
            address1_input.send_keys(address1)
        except Exception as e:
            print("failed to set address1")

    def set_address2(self, address2):
        try:
            address2_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.address2))
            )
            address2_input.clear()
            address2_input.send_keys(address2)
        except Exception as e:
            print("failed to set address 2 ")

    def set_country(self):
        try:
            country_input = Select(
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((self.country_dropdown))
                )
            )
            country_input.select_by_value("India")
        except Exception as e:
            print("failed to set country!")

    def set_state(self, state):
        try:
            state_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.state))
            )
            state_input.clear()
            state_input.send_keys(state)
        except Exception as e:
            print("failed to set state!")

    def set_city(self, city):
        try:
            city_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.city))
            )
            city_input.clear()
            city_input.send_keys(city)
        except Exception as e:
            print("failed to set city")

    def set_zipcode(self, zipcode):
        try:
            zipcode_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.zipcode))
            )
            zipcode_input.clear()
            zipcode_input.send_keys(zipcode)
        except Exception as e:
            print("failed to set zipcode")

    def set_mobilenumber(self, mobile_number):
        try:
            mobilenumber_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.mobileNumber))
            )
            mobilenumber_input.clear()
            mobilenumber_input.send_keys(mobile_number)
        except Exception as e:
            print("failed to set mobile number!")

    def click_create_account(self):
        try:
            click_account = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.create_account))
            )
            click_account.click()
        except Exception as e:
            print("failed to create account")

    def is_user_logged_in(self):
        try:
            sucesselement = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[@id='form']/div/div/div/h2/b")
                )
            )
            assert sucesselement.text == "ACCOUNT CREATED!"
            return True
        except Exception:
            print("failed to login!")
            return False

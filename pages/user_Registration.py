import random
import string
import time

# from utils.logger import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def generate_unique_email(base_email="testuser"):
    timestamp = int(time.time())
    random_str = "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"{base_email}_{timestamp}_{random_str}@example.com"


class UserRegistration:
    def __init__(self, driver):
        self.driver = driver
        self.baseUrl = "https://automationexercise.com/login"

        self.name_input = (By.XPATH, "//input[@placeholder='Name']")
        self.email_input = (By.XPATH, "//input[@data-qa='signup-email']")
        self.signUp_button = (By.XPATH, "//button[normalize-space()='Signup']")

    def navigate_to_registration_page(self):
        self.driver.get(self.baseUrl)

    def setName(self, name):
        try:
            name_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.name_input))
            )
            name_input.clear()
            name_input.send_keys(name)
        except Exception as e:
            print("fialed to set name!")

    def setEmail(self):
        try:
            unique_email = generate_unique_email()
            email_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.email_input))
            )
            email_input.clear()
            email_input.send_keys(unique_email)
            print(f"Using unique email: {unique_email}")
        except Exception as e:
            print("failed to set email!")

    def click_signUp(self):
        try:
            email_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((self.signUp_button))
            )
            email_input.click()
        except Exception as e:
            print("Failed to signup")

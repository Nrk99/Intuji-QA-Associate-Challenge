import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Product:

    def __init__(self, driver):
        self.driver = driver

        self.product_navigation = (
            By.XPATH,
            "//*[@id='header']/div/div/div/div[2]/div/ul/li[2]",
        )
        self.expand_womendress = (
            By.XPATH,
            "//*[@id='accordian']/div[1]/div[1]/h4/a/span",
        )
        self.select_dress = (By.XPATH, "//*[@id='Women']/div/ul/li[1]/a")
        self.view_product = (
            By.XPATH,
            "/html/body/section/div/div[2]/div[2]/div/div[2]/div/div[2]/ul/li/a",
        )
        self.prodct_category_locator = (
            By.XPATH,
            "/html/body/section/div/div[2]/div[2]/div/h2",
        )
        self.product_name_locator = (By.XPATH, "//div[@class='product-information']/h2")

        self.product_price = (
            By.XPATH,
            "/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/span",
        )
        self.product_availability = (
            By.XPATH,
            "/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[2]",
        )

        self.productBabyhug = (
            By.XPATH,
            "//a[@href='/brand_products/Babyhug' and contains(., 'Babyhug')]",
        )

        self.continue_shopping_button = (
            By.XPATH,
            "//*[@id='cartModal']/div/div/div[3]/button",
        )

        self.add_to_cart = (
            By.XPATH,
            "//button[@type='button' and contains(., 'Add to cart')]",
        )
        self.view_cart = (By.XPATH, "(//a[@href='/view_cart'])[2]")
        self.polo = (By.XPATH, "//a[@href='/brand_products/Polo']")
        self.card1 = (
            By.XPATH,
            "/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]",
        )
        self.card2 = (
            By.XPATH,
            "/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[2]",
        )
        self.cross = (By.XPATH, "//tr[@id='product-1']//i[@class='fa fa-times']")
        self.checkout = (By.XPATH, "//a[@class='btn btn-default check_out']")
        self.total_price = (By.XPATH, "//*[@id='cart_info']/table/tbody/tr[3]")
        self.place_order = (By.XPATH, "//a[@class='btn btn-default check_out']")
        self.name_on_card = (By.NAME, "name_on_card")
        self.card_number = (By.NAME, "card_number")
        self.cvc_number = (By.NAME, "cvc")
        self.expiration_month_number = (By.NAME, "expiry_month")
        self.expiration_year_number = (By.NAME, "expiry_year")
        self.pay_order_button = (By.ID, "submit")
        self.logout = (By.XPATH, "//a[normalize-space()='Logout']")

    def click_product(self):
        click_product = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((self.product_navigation))
        )
        click_product.click()

    def click_expand_women_dress(self):
        try:
            click_womendress = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.expand_womendress))
            )
            click_womendress.click()
        except Exception as e:
            print("unable to expand women dress")

    def click_dress(self):
        try:
            click_women_dress = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.select_dress))
            )
            click_women_dress.click()
        except Exception as e:
            print("failed to click on dress!")

    def verify_category_name(self, expected_name="WOMEN - DRESS PRODUCTS"):
        try:
            product_catrgory_name = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.prodct_category_locator)
            )
            category_name = product_catrgory_name.text.strip()
            category_name = re.sub(r"\s+", " ", category_name)

            assert (
                category_name == expected_name
            ), f"Expected: '{expected_name}', but got: '{category_name}'"
            print("✅ Product Category name verified:", category_name)
        except Exception as e:
            print(f"Verification failed: {e}")
            raise

    def click_view_product(self):
        try:
            click_view_product = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.view_product))
            )
            click_view_product.click()
        except Exception as e:
            print("failed to click on view product!")

    def click_polo(self):
        try:
            click_polo_product = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.polo))
            )
            click_polo_product.click()
        except Exception as e:
            print("unable to click on polo")

    def delete_product(self):
        try:
            cross_product = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.cross))
            )
            cross_product.click()
        except Exception as e:
            print("failed to delete product")

    def procees_to_checkout(self):
        try:
            checkout_product = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.checkout))
            )
            checkout_product.click()
        except Exception as e:
            print("failed to checkout!")

    def add_product_to_cart1(self):
        try:
            add_product1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.add_to_cart))
            )
            add_product1.click()
            continue_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[text()='Continue Shopping']")
                )
            )
            continue_btn.click()
        except Exception as e:
            print("unable to add product in cart1")

    def add_product_to_cart2(self):
        try:
            add_product2 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.add_to_cart))
            )
            add_product2.click()
            continue_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[text()='Continue Shopping']")
                )
            )
            continue_btn.click()
        except Exception as e:
            print("unable to add product to  ")

    def verify_product_name(self, expected_name="Sleeveless Dress"):
        try:
            product_name_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.product_name_locator)
            )
            product_name = product_name_element.text.strip()
            product_name = re.sub(r"\s+", " ", product_name)

            assert (
                product_name == expected_name
            ), f"Expected: '{expected_name}', but got: '{product_name}'"
            print("✅ Product name verified:", product_name)
        except Exception as e:
            print(f"Verification failed: {e}")
            raise

    def verify_product_price(self, expected_name="Rs. 1000"):
        try:
            product_price_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.product_price)
            )
            product_price = product_price_element.text.strip()
            product_price = re.sub(r"\s+", " ", product_price)

            assert (
                product_price == expected_name
            ), f"Expected: '{expected_name}', but got: '{product_price}'"
            print("✅ Product Price verified:", product_price)
        except Exception as e:
            print(f"Verification failed: {e}")
            raise

    def verify_stock_availability(self):
        try:
            stock_status_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.product_availability))
            )
            stock_status = stock_status_element.text.strip().lower()
            if "in stock" in stock_status:
                print("✅ Product is in stock.")
                return True
            else:
                print("❌ Product is out of stock.")
                return False
        except Exception as e:
            print(f"Error while checking stock availability: {e}")
            return False

    def choose_new_product_category(self):
        try:
            choose_product = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.productBabyhug))
            )
            choose_product.click()
        except Exception as e:
            print("Error while clicking to product!")
            return False

    def add_product_multiple_times(self, times):
        try:
            for i in range(times):
                # Click 'Add to Cart' button
                WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable(self.add_to_cart)
                ).click()

                if i < times - 1:
                    # Wait for 'Continue Shopping' button and click it
                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(self.continue_shopping_button)
                    ).click()
                else:
                    # Wait for 'View Cart' button and click it
                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(self.view_cart)
                    ).click()
        except Exception as e:
            print("Failed to add multiple product!")

    def verify_total_product_price(self, expected_price=2497):
        # Wait for any element with class 'cart_total_price'
        price_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((self.total_price))
        )

        price_text = price_element.text.strip()  # e.g., "Rs. 2,497"

        # Remove non-numeric characters to extract the number
        numeric_price = int("".join(filter(str.isdigit, price_text)))  # becomes 2497

        # Compare with expected
        assert (
            numeric_price == expected_price
        ), f"❌ Price mismatch! Expected: {expected_price}, Found: {numeric_price}"
        print(f"✅ Product price verified: ₹{numeric_price}")

    def click_place_order(self):
        try:
            place_order_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.place_order)
            )
            place_order_element.click()
        except Exception as e:
            print("failed to place order!")

    def name_card(self):
        try:
            card_name_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.name_on_card)
            )
            card_name_element.clear()
            card_name_element.send_keys("Ashish Shrestha")
        except Exception as e:
            print("Failed to enter the name on card!")

    def enter_card_number(self):
        try:
            card_number_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.card_number)
            )
            card_number_element.clear()
            card_number_element.send_keys("444455554444")
        except Exception as e:
            print("Failed to enter the name on card!")

    def enter_cvc(self):
        try:
            cvc_number_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.cvc_number)
            )
            cvc_number_element.clear()
            cvc_number_element.send_keys("132")
        except Exception as e:
            print("Failed to enter the cvc on card!")

    def enter_expiary_month(self):
        try:
            expiray_month_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.expiration_month_number)
            )
            expiray_month_element.clear()
            expiray_month_element.send_keys("10")
        except Exception as e:
            print("Failed to enter the month on card!")

    def enter_expiary_year(self):
        try:
            expiary_year_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.expiration_year_number)
            )
            expiary_year_element.clear()
            expiary_year_element.send_keys("2025")
        except Exception as e:
            print("Failed to enter the year on card!")

    def pay_and_confirm_order(self):
        try:
            pay_order_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.pay_order_button)
            )
            pay_order_element.click()
        except Exception as e:
            print("Failed to clickk on pay order card!")

    def verify_order_placed(self):
        try:
            order_placed_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//b[normalize-space()='Order Placed!']")
                )
            )
            assert (
                order_placed_element.is_displayed()
            ), "❌ 'Order Placed!' text not displayed"
            print("✅ 'Order Placed!' message verified successfully.")
        except Exception as e:
            print("❌ Failed to verify 'Order Placed!' message:", e)

    def click_logout(self):
        try:
            logout_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.logout)
            )
            logout_element.click()
        except Exception as e:
            print("Failed to login!")

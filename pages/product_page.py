from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    # Локаторы внутри класса
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")
    MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert-info strong")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    def add_product_to_cart(self):
        add_button = self.browser.find_element(*self.ADD_TO_CART_BUTTON)
        add_button.click()

    def get_product_name(self):
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def should_be_correct_product_name_in_message(self, expected_name):
        name_in_message = self.browser.find_element(*self.MESSAGE_PRODUCT_NAME).text
        assert name_in_message == expected_name, f"Expected product name '{expected_name}', but got '{name_in_message}'"

    def should_be_correct_price_in_message(self, expected_price):
        price_in_message = self.browser.find_element(*self.MESSAGE_PRODUCT_PRICE).text
        assert price_in_message == expected_price, f"Expected price '{expected_price}', but got '{price_in_message}'"

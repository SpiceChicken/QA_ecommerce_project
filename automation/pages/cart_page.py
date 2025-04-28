from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.NAME, "search")
        self.search_button = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")
        self.add_to_cart_button = (By.CSS_SELECTOR, ".product-layout .product-thumb button[onclick*='cart.add']")
        self.cart_total = (By.ID, "cart-total")

    def load_home(self):
        self.driver.get("https://demo.opencart.com/")

    def search_product(self, keyword):
        self.driver.find_element(*self.search_input).clear()
        self.driver.find_element(*self.search_input).send_keys(keyword)
        self.driver.find_element(*self.search_button).click()

    def add_first_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def get_cart_total_text(self):
        return self.driver.find_element(*self.cart_total).text

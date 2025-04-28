from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.NAME, "search")
        self.search_button = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")
        self.product_list = (By.CSS_SELECTOR, ".product-layout .product-thumb")

    def load(self):
        self.driver.get("https://demo.opencart.com/")

    def search_product(self, keyword):
        self.driver.find_element(*self.search_input).clear()
        self.driver.find_element(*self.search_input).send_keys(keyword)
        self.driver.find_element(*self.search_button).click()

    def get_search_results(self):
        return self.driver.find_elements(*self.product_list)

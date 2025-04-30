from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_input = (By.NAME, "search")
        self.search_button = (By.CSS_SELECTOR, "button.btn.btn-light")
        self.product_list = (By.CSS_SELECTOR, ".product-thumb")
        self.no_result = (By.XPATH, "//*[contains(text(), 'There is no product that matches the search criteria.')]")

    def load(self):
        self.driver.get("http://localhost/")
        self.wait_for_visible(self.search_input)

    def search(self, keyword):
        self.type_text(self.search_input, keyword)
        self.click(self.search_button)

    def has_results(self):
        self.wait_for_present(self.product_list)  # 목록 요소 로드 대기
        return len(self.driver.find_elements(*self.product_list)) > 0

    def is_no_result_message_visible(self):
        return len(self.driver.find_elements(*self.no_result)) > 0

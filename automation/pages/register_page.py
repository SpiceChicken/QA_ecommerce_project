# automation/pages/register_page.py
from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage

class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name = (By.ID, "input-firstname")
        self.last_name = (By.ID, "input-lastname")
        self.email = (By.ID, "input-email")
        self.password = (By.ID, "input-password")
        self.privacy_policy_checkbox = (By.NAME, "agree")
        self.continue_button = (By.CSS_SELECTOR, "button.btn.btn-primary")

    def load(self):
        self.driver.get("http://localhost/index.php?route=account/register")

    def register_user(self, first, last, email, password):
        self.type_text(self.first_name, first)
        self.type_text(self.last_name, last)
        self.type_text(self.email, email)
        self.type_text(self.password, password)
        self.click(self.privacy_policy_checkbox)
        self.click(self.continue_button)

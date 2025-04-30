from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_input = (By.ID, "input-email")
        self.password_input = (By.ID, "input-password")
        self.login_button = (By.CSS_SELECTOR, "input.btn.btn-primary")

    def load(self):
        self.driver.get("http://localhost/index.php?route=account/login")

    def login(self, email, password):
        self.type_text(self.email_input, email)
        self.type_text(self.password_input, password)
        self.click(self.login_button)

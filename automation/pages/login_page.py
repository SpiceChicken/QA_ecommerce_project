from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "input-email")
        self.password_input = (By.ID, "input-password")
        self.login_button = (By.CSS_SELECTOR, "input.btn.btn-primary")

    def load(self):
        self.driver.get("https://demo.opencart.com/index.php?route=account/login")

    def login(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

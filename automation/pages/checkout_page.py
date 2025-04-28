from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.ID, "cart-total")
        self.view_cart_link = (By.LINK_TEXT, "View Cart")
        self.checkout_button = (By.LINK_TEXT, "Checkout")
        self.billing_details_continue = (By.ID, "button-payment-address")
        self.delivery_details_continue = (By.ID, "button-shipping-address")
        self.delivery_method_continue = (By.ID, "button-shipping-method")
        self.terms_checkbox = (By.NAME, "agree")
        self.payment_method_continue = (By.ID, "button-payment-method")
        self.confirm_order_button = (By.ID, "button-confirm")
        self.success_message = (By.CSS_SELECTOR, "#content h1")

    def open_cart(self):
        self.driver.find_element(*self.cart_button).click()
        self.driver.find_element(*self.view_cart_link).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def complete_checkout_steps(self):
        self.driver.find_element(*self.billing_details_continue).click()
        self.driver.find_element(*self.delivery_details_continue).click()
        self.driver.find_element(*self.delivery_method_continue).click()
        self.driver.find_element(*self.terms_checkbox).click()
        self.driver.find_element(*self.payment_method_continue).click()
        self.driver.find_element(*self.confirm_order_button).click()

    def get_success_message(self):
        return self.driver.find_element(*self.success_message).text

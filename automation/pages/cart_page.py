from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage
import time

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_input = (By.NAME, "search")
        self.search_button = (By.CSS_SELECTOR, "button.btn.btn-light")
        self.product_link = (By.CSS_SELECTOR, ".product-thumb h4 a")
        self.add_to_cart = (By.ID, "button-cart")
        self.cart_button = (By.ID, "cart")
        self.view_cart_link = (By.XPATH, "//strong[text()=' View Cart']")
        self.cart_items = (By.ID, "output-cart")
        self.quantity_input = (By.CSS_SELECTOR, "input[name*='quantity']")
        self.update_button = (By.CSS_SELECTOR, "button[formaction*='checkout/cart.edit']")
        self.remove_button = (By.CSS_SELECTOR, "a[href*='checkout/cart.remove']")
        self.empty_message = (By.XPATH, "//*[contains(text(), 'Your shopping cart is empty!')]")

    def load_home(self):
        self.driver.get("http://localhost/")
        self.wait_for_visible(self.search_input)

    def search_and_open_product(self, keyword):
        self.type_text(self.search_input, keyword)
        self.click(self.search_button)
        time.sleep(2)  # 검색 결과 로딩 대기
        product_link = self.wait_for_clickable(self.product_link)
        product_link.click()
        time.sleep(2)  # 제품 페이지 로딩 대기

    def add_to_cart_click(self):
        self.click(self.add_to_cart)
        time.sleep(3)  # 장바구니 추가 완료 대기

    def go_to_cart(self):
        self.click(self.cart_button)
        self.wait_for_clickable(self.view_cart_link)  # 장바구니 드롭다운 메뉴 표시 대기
        self.click(self.view_cart_link)
        self.wait_for_visible(self.cart_items)  # 장바구니 페이지 로딩 대기

    def get_cart_item_count(self):
        return len(self.driver.find_elements(*self.cart_items))

    def update_quantity(self, new_quantity):
        input_field = self.wait_for_visible(self.quantity_input)
        input_field.clear()
        input_field.send_keys(str(new_quantity))
        self.wait_for_clickable(self.update_button)  # 업데이트 버튼이 클릭 가능한 상태가 될 때까지 대기
        self.click(self.update_button)
        self.wait_for_visible(self.cart_items)  # 수량 업데이트 완료 대기

    def remove_product(self):
        self.wait_for_clickable(self.remove_button)  # 제거 버튼이 클릭 가능한 상태가 될 때까지 대기
        self.click(self.remove_button)
        time.sleep(2)  # 제거 요청 처리 및 페이지 새로고침 대기

    def is_cart_empty(self):
        return len(self.driver.find_elements(*self.empty_message)) > 0

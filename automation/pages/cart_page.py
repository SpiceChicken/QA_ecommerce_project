from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_input = (By.NAME, "search")
        self.search_button = (By.CSS_SELECTOR, "button.btn.btn-light")
        self.product_link = (By.CSS_SELECTOR, ".product-thumb h4 a")
        self.add_to_cart = (By.ID, "button-cart")
        self.cart_button = (By.ID, "cart")
        self.view_cart_link = (By.XPATH, "//strong[text()=' View Cart']")
        self.checkout_link = (By.CSS_SELECTOR, "a.btn.btn-primary")
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

    def go_to_checkout(self):
        """장바구니에서 체크아웃 페이지로 이동"""
        try:
            self.wait_for_clickable(self.checkout_link)
            self.click(self.checkout_link)

            # URL 전환 대기
            WebDriverWait(self.driver, 20).until(EC.url_contains("checkout/checkout"))

            # Checkout 페이지 주요 요소가 로딩될 때까지 대기 (예: 이름 입력란)
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.ID, "input-payment-firstname"))
            )

            return True
        except Exception as e:
            print(f"체크아웃 페이지 이동 실패: {str(e)}")
            return False

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

    def select_dropdown(self, locator, index=1):
        dropdown_element = self.wait_for_visible(locator)
        dropdown = Select(dropdown_element)
        
        # 활성화된 옵션만 필터링
        options = dropdown.options
        enabled_options = [opt for opt in options if opt.is_enabled() and opt.get_attribute("value")]
        
        if len(enabled_options) > index:
            enabled_options[index].click()
        else:
            raise ValueError(f"선택 가능한 드롭다운 옵션이 부족합니다 (index={index})")

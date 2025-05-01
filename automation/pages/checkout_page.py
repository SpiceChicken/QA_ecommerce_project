from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import time

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Your Personal Details
        self.first_name = (By.ID, "input-firstname")
        self.last_name = (By.ID, "input-lastname")
        self.email = (By.ID, "input-email")
        # shipping
        self.address = (By.ID, "input-shipping-address-1")
        self.city = (By.ID, "input-shipping-city")
        self.postcode = (By.ID, "input-shipping-postcode")
        self.country = (By.ID, "input-shipping-country")
        self.zone = (By.ID, "input-shipping-zone")
        self.terms_checkbox = (By.NAME, "agree")
        
        # Your Password
        self.password = (By.ID, "input-password")
        self.confirm_order_button = (By.ID, "button-register")

        # Success
        self.order_success_message = (By.XPATH, "//*[contains(text(), 'Success')]")
        self.order_fail_message = (By.XPATH, "//*[contains(text(), 'Warning')]") 

        # Checkout
        self.checkout_form = (By.ID, "checkout-register")
        self.billing_form = (By.ID, "checkout-payment-method")

        #Alert
        self.alert_message = (By.CSS_SELECTOR, ".alert-danger")

    def wait_for_checkout_page(self):
        try:
            self.wait_for_visible(self.checkout_form, timeout=10)
            self.wait_for_visible(self.billing_form, timeout=10)
            return True
        except Exception as e:
            print(f"페이지 로딩 실패: {str(e)}")
            return False

    def fill_billing_details(self, first, last, email, address, city, postcode, country_index=1, zone_index=1):
        if not self.wait_for_checkout_page():
            raise Exception("체크아웃 페이지 로딩 실패")
        time.sleep(2)

        try:
            self.type_text(self.first_name, first)
            self.type_text(self.last_name, last)
            self.type_text(self.email, email)
            self.type_text(self.address, address)
            self.type_text(self.city, city)
            self.type_text(self.postcode, postcode)
            self.select_dropdown(self.country, index=country_index)
            time.sleep(2)
            self.select_dropdown(self.zone, index=zone_index)
            time.sleep(1)
        except Exception as e:
            print(f"결제 정보 입력 실패: {str(e)}")
            raise

    def is_order_successful(self):
        try:
            self.wait_for_visible(self.order_success_message, timeout=10)
            return True
        except:
            return False

    def is_order_failed(self):
        try:
            self.wait_for_visible(self.order_fail_message, timeout=10)
            return True
        except:
            return False

    def input_password(self, password):
        """비밀번호를 입력합니다."""
        time.sleep(2)
        self.wait_for_visible(self.password)
        self.type_text(self.password, password)

    def accept_terms(self):
        self.wait_for_clickable(self.terms_checkbox)
        self.click(self.terms_checkbox)

    def place_order(self):
        self.wait_for_clickable(self.confirm_order_button)
        self.click(self.confirm_order_button)

    def select_dropdown(self, locator, index=1):
        dropdown_element = self.wait_for_visible(locator)
        dropdown = Select(dropdown_element)
        options = dropdown.options
        enabled_options = [opt for opt in options if opt.is_enabled() and opt.get_attribute("value")]
        if len(enabled_options) > index:
            enabled_options[index].click()
        else:
            raise ValueError(f"선택 가능한 드롭다운 옵션이 부족합니다 (index={index})")

    def is_session_active(self):
        """세션이 유효한지 확인합니다."""
        try:
            # 사용자 메뉴가 표시되는지 확인
            self.wait_for_visible(self.checkout_form, timeout=5)
            # 로그아웃 버튼이 존재하는지 확인
            self.wait_for_visible(self.billing_form, timeout=5)
            return True
        except:
            return False
    def wait_for_checkout_page(self):
        """체크아웃 페이지가 완전히 로드될 때까지 대기"""
        try:
            # 결제 정보 입력 필드 중 첫 번째 요소가 로딩될 때까지 대기
            self.wait_for_visible(self.first_name, timeout=15)
            return True
        except Exception as e:
            print(f"페이지 로딩 실패: {str(e)}")
            print(f"현재 URL: {self.driver.current_url}")
            print(f"페이지 제목: {self.driver.title}")
            print(f"HTML 일부:\n{self.driver.page_source[:500]}")  # 앞부분만 출력
            return False


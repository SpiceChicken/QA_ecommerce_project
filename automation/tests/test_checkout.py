import pytest
import time
from selenium import webdriver
from automation.pages.cart_page import CartPage
from automation.pages.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_checkout_process(driver):
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Step 1: 상품 검색하고 장바구니 담기
    cart_page.load_home()
    cart_page.search_product("MacBook")
    cart_page.add_first_product_to_cart()
    time.sleep(2)

    # Step 2: 장바구니 열기
    checkout_page.open_cart()

    # Step 3: Checkout 진행
    checkout_page.proceed_to_checkout()

    # Step 4: Checkout 단계 완료
    checkout_page.complete_checkout_steps()

    # Step 5: 성공 메시지 확인
    success_message = checkout_page.get_success_message()
    assert "Your order has been placed!" in success_message, f"주문이 완료되지 않았습니다: {success_message}"

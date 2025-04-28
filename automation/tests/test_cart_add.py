import pytest
from selenium import webdriver
from automation.pages.cart_page import CartPage
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_add_product_to_cart(driver):
    cart_page = CartPage(driver)
    cart_page.load_home()
    cart_page.search_product("MacBook")
    cart_page.add_first_product_to_cart()
    
    time.sleep(2)  # 잠깐 대기 (알림창 뜨는 타이밍 고려)
    
    cart_text = cart_page.get_cart_total_text()
    assert "1 item(s)" in cart_text or "1상품" in cart_text, f"장바구니에 상품이 추가되지 않았습니다: {cart_text}"

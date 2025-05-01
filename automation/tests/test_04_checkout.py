import pytest
from selenium import webdriver
from automation.pages.cart_page import CartPage
from automation.pages.checkout_page import CheckoutPage
from automation.utils.test_data import get_registered_user
from selenium.webdriver.common.by import By
import time

user = get_registered_user()

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_tc015_successful_checkout(driver):
    cart = CartPage(driver)

    # 상품 추가 및 장바구니 이동
    cart.load_home()
    cart.search_and_open_product("MacBook")
    cart.add_to_cart_click()
    cart.go_to_cart()
    
    # 체크아웃 이동
    cart.go_to_checkout()
    checkout = CheckoutPage(driver)  # 이 시점 이후에 생성해야 요소 접근 가능

    # 결제 진행
    checkout.fill_billing_details(
        first=user["first_name"],
        last=user["last_name"],
        email=user["email"],
        address="123 Main",
        city="Seoul",
        postcode="12345"
    )
    checkout.input_password(user["password"])

    checkout.accept_terms()
    checkout.place_order()

    assert checkout.is_order_successful()

def test_tc016_checkout_with_different_address(driver):
    cart = CartPage(driver)

    cart.load_home()
    cart.search_and_open_product("MacBook")
    cart.add_to_cart_click()
    cart.go_to_cart()

    cart.go_to_checkout()
    checkout = CheckoutPage(driver)

    checkout.fill_billing_details(
        first=user["first_name"],
        last=user["last_name"],
        email=user["email"],
        address="456 Sub",
        city="Busan",
        postcode="54321"
    )
    checkout.input_password(user["password"])
    
    checkout.accept_terms()
    checkout.place_order()

    assert checkout.is_order_failed()

def test_tc017_checkout_without_agreeing_terms(driver):
    cart = CartPage(driver)
    cart.load_home()
    cart.search_and_open_product("MacBook")
    cart.add_to_cart_click()
    cart.go_to_cart()

    cart.go_to_checkout()
    checkout = CheckoutPage(driver)

    checkout.fill_billing_details(
        first="No", last="Agree", email="noagree@example.com",
        address="789 Else", city="Daegu", postcode="67890"
    )
    checkout.input_password(user["password"])
    # checkout.accept_terms()
    checkout.place_order()

    # 약관 동의 없이 주문 시도
    checkout.click(checkout.confirm_order_button)

    assert checkout.is_order_failed()

def test_tc018_refresh_during_checkout(driver):
    cart = CartPage(driver)

    cart.load_home()
    cart.search_and_open_product("MacBook")
    cart.add_to_cart_click()
    cart.go_to_cart()

    cart.go_to_checkout()
    checkout = CheckoutPage(driver)

    checkout.fill_billing_details(
        first="Refresh", last="Test", email=user["email"],
        address="123 Refresh", city="Seoul", postcode="00000"
    )
    checkout.input_password(user["password"])

    driver.refresh()
    checkout.wait_for_visible(checkout.first_name)

    checkout.accept_terms()
    checkout.place_order()

    assert checkout.is_session_active()
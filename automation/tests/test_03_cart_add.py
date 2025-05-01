import pytest
from selenium import webdriver
from automation.pages.cart_page import CartPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_tc011_add_to_cart(driver):
    cart = CartPage(driver)
    cart.load_home()
    cart.search_and_open_product("MacBook")
    cart.add_to_cart_click()
    cart.go_to_cart()
    assert cart.get_cart_item_count() == 1

def test_tc012_add_same_product_twice(driver):
    cart = CartPage(driver)
    cart.load_home()
    cart.search_and_open_product("MacBook")
    cart.add_to_cart_click()
    cart.add_to_cart_click()
    cart.go_to_cart()
    qty = cart.driver.find_element(*cart.quantity_input).get_attribute("value")
    assert qty == "2"

def test_tc013_remove_product(driver):
    cart = CartPage(driver)
    cart.load_home()
    cart.search_and_open_product("MacBook")
    cart.add_to_cart_click()
    cart.go_to_cart()
    cart.remove_product()
    assert cart.is_cart_empty()

def test_tc014_update_quantity(driver):
    cart = CartPage(driver)
    cart.load_home()
    cart.search_and_open_product("MacBook")
    cart.add_to_cart_click()
    cart.go_to_cart()
    cart.update_quantity(1)
    qty = cart.driver.find_element(*cart.quantity_input).get_attribute("value")
    assert qty == "1"

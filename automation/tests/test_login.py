import pytest
from selenium import webdriver
from automation.pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("valid_email@example.com", "valid_password")
    assert "My Account" in driver.title

def test_login_failure(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("invalid@example.com", "wrongpassword")
    alert = driver.find_element("css selector", ".alert-danger")
    assert "Warning" in alert.text
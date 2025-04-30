import pytest
from selenium import webdriver
from automation.pages.search_page import SearchPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_tc006_exact_keyword_search(driver):
    page = SearchPage(driver)
    page.load()
    page.search("MacBook")
    assert page.has_results()

def test_tc007_incorrect_keyword_search(driver):
    page = SearchPage(driver)
    page.load()
    page.search("asdfasdfasdf")
    assert page.is_no_result_message_visible()

def test_tc008_blank_search(driver):
    page = SearchPage(driver)
    page.load()
    page.search(" ")
    assert page.is_no_result_message_visible()

def test_tc009_case_insensitive_search(driver):
    page = SearchPage(driver)
    page.load()
    page.search("macbook")
    results_lower = page.has_results()

    page.load()
    page.search("MACBOOK")
    results_upper = page.has_results()

    assert results_lower and results_upper

def test_tc010_special_characters_search(driver):
    page = SearchPage(driver)
    page.load()
    page.search("@#$%")
    assert page.is_no_result_message_visible()

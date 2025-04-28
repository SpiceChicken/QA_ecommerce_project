import pytest
from selenium import webdriver
from automation.pages.search_page import SearchPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_search_existing_product(driver):
    search_page = SearchPage(driver)
    search_page.load()
    search_page.search_product("MacBook")
    results = search_page.get_search_results()
    assert len(results) > 0, "검색 결과가 없습니다."

def test_search_non_existing_product(driver):
    search_page = SearchPage(driver)
    search_page.load()
    search_page.search_product("nonexistentproduct12345")
    results = search_page.get_search_results()
    assert len(results) == 0, "검색 결과가 없어야 합니다."

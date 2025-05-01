# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from automation.pages.login_page import LoginPage
# from automation.utils.test_data import get_registered_user
# from selenium.webdriver.support.ui import WebDriverWait # WebDriverWait 임포트
# from selenium.webdriver.support import expected_conditions as EC # expected_conditions 임포트

# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     yield driver
#     driver.quit()

# def test_tc001_login_success(driver):
#     # 등록된 사용자 정보 가져오기
#     user = get_registered_user()
    
#     # 로그인 페이지 로드
#     login_page = LoginPage(driver)
#     login_page.load()
    
#     # 로그인 수행
#     login_page.login(user["email"], user["password"])
    
#     # 로그인 성공 확인
#     wait = WebDriverWait(driver, 10) # driver 객체와 최대 대기 시간 설정
#     # expected_conditions.title_contains() 조건을 사용하여 제목 대기
#     wait.until(EC.title_contains("My Account"))
#     assert "My Account" in driver.title

# def test_tc002_wrong_password(driver):
#     user = get_registered_user()
#     login_page = LoginPage(driver)
#     login_page.load()
#     login_page.login(user["email"], "wrongpass123")
    
#     alert = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
#     )
#     assert "Warning" in alert.text


# def test_tc003_nonexistent_email(driver):
#     login_page = LoginPage(driver)
#     login_page.load()
#     login_page.login("nonexist@example.com", "irrelevant123")
    
#     alert = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
#     )
#     assert "Warning" in alert.text


# def test_tc004_missing_email(driver):
#     login_page = LoginPage(driver)
#     login_page.load()
#     driver.find_element(By.ID, "input-password").send_keys("password123")
#     driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
#     alert = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
#     )
#     assert "Warning" in alert.text



# def test_tc005_missing_password(driver):
#     login_page = LoginPage(driver)
#     login_page.load()
#     driver.find_element(By.ID, "input-email").send_keys("test@example.com")
#     driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
#     alert = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
#     )
#     assert "Warning" in alert.text
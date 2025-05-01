# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from automation.pages.register_page import RegisterPage
# import random
# from automation.utils.test_data import set_registered_user, get_registered_user
# from selenium.webdriver.support.ui import WebDriverWait # WebDriverWait 임포트
# from selenium.webdriver.support import expected_conditions as EC # expected_conditions 임포트

# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     yield driver
#     driver.quit()

# def test_register_user(driver):
#     # 테스트 데이터 생성
#     first_name = "Test"
#     last_name = "User"
#     unique_email = f"testuser_{random.randint(1000,9999)}@example.com"
#     password = "Test123!"
    
#     # 등록 페이지 로드
#     register_page = RegisterPage(driver)
#     register_page.load()
    
#     # 사용자 등록
#     register_page.register_user(first_name, last_name, unique_email, password)

#     # 페이지 제목이 "Your Account Has Been Created!"를 포함할 때까지 최대 10초 대기
#     wait = WebDriverWait(driver, 10) # driver 객체와 최대 대기 시간 설정
#     # expected_conditions.title_contains() 조건을 사용하여 제목 대기
#     wait.until(EC.title_contains("Your Account Has Been Created!"))
    
#     # 등록 성공 확인
#     assert "Your Account Has Been Created!" in driver.title
    
#     # 등록된 사용자 정보 저장
#     set_registered_user(unique_email, password, first_name, last_name)
#     print(f"등록된 사용자 이메일: {unique_email}")

# def test_register_duplicate_user(driver):
#     user = get_registered_user()
#     # 테스트 데이터 생성
#     first_name = user["first_name"]
#     last_name = user["last_name"]
#     unique_email = user["email"]
#     password = user["password"]
    
#     # 등록 페이지 로드
#     register_page = RegisterPage(driver)
#     register_page.load()
    
#     # 사용자 등록
#     register_page.register_user(first_name, last_name, unique_email, password)
    
#     # 가입 실패 확인
#     alert = driver.find_element(By.CSS_SELECTOR, ".alert-danger")
    
#     assert "Warning" in alert.text
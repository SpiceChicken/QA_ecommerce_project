from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # WebDriverWait 임포트
from selenium.webdriver.support import expected_conditions as EC # expected_conditions 임포트
# import time # time 모듈은 더 이상 필요 없을 수 있으므로 삭제하거나 주석 처리

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "input-firstname")
        self.last_name = (By.ID, "input-lastname")
        self.email = (By.ID, "input-email")
        # self.telephone = (By.ID, "input-telephone")
        self.password = (By.ID, "input-password")
        # self.confirm_password = (By.ID, "input-confirm")
        self.privacy_policy_checkbox = (By.NAME, "agree")
        self.continue_button = (By.CSS_SELECTOR, "button.btn.btn-primary") # 계속 버튼 로케이터 정의

    def load(self):
        self.driver.get("http://localhost/index.php?route=account/register")
        # 페이지 로드 완료 대기 (선택 사항, 필요한 경우 추가)
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.first_name))


    def register_user(self, first, last, email, password): # phone 인자 추가
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.email).send_keys(email)
        # self.driver.find_element(*self.telephone).send_keys(phone)
        self.driver.find_element(*self.password).send_keys(password)
        # self.driver.find_element(*self.confirm_password).send_keys(password)

        # JavaScript Executor를 사용하여 체크박스 상태를 설정 (이전에 적용한 코드 유지)
        privacy_checkbox_element = self.driver.find_element(*self.privacy_policy_checkbox)
        self.driver.execute_script("arguments[0].checked = true;", privacy_checkbox_element)

        # time.sleep(2) # <--- 이 줄을 삭제합니다.

        # Continue 버튼이 클릭 가능한 상태가 될 때까지 최대 10초 대기
        # WebDriverWait 객체를 생성합니다. (driver, 최대 대기 시간(초))
        wait = WebDriverWait(self.driver, 10)
        
        # expected_conditions.element_to_be_clickable 조건을 사용하여 요소가 클릭 가능해질 때까지 대기합니다.
        # wait.until() 메서드는 조건이 만족되면 해당 WebElement를 반환합니다.
        continue_button_element = wait.until(EC.element_to_be_clickable(self.continue_button))

        # 대기가 끝난 후, 반환된 요소(continue_button_element)를 클릭합니다.
        continue_button_element.click()
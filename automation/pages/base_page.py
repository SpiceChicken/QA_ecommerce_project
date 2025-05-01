from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.logger = logging.getLogger(__name__)

    def wait_for_visible(self, locator, timeout=None):
        timeout = timeout or self.timeout
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            msg = f"[VISIBLE TIMEOUT] 요소 {locator} 가 {timeout}초 내에 보이지 않음"
            self.logger.error(msg)
            raise Exception(msg)

    def wait_for_clickable(self, locator, timeout=None):
        timeout = timeout or self.timeout
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            msg = f"[CLICKABLE TIMEOUT] 요소 {locator} 가 {timeout}초 내에 클릭 불가 상태"
            self.logger.error(msg)
            raise Exception(msg)

    def click(self, locator):
        try:
            element = self.wait_for_clickable(locator)
            element.click()
            self.logger.debug(f"[CLICK] 요소 클릭 성공: {locator}")
        except Exception as e:
            self.logger.error(f"[CLICK ERROR] 요소 클릭 실패: {locator} - {str(e)}")
            raise

    def type_text(self, locator, text):
        try:
            element = self.wait_for_visible(locator)
            element.clear()
            element.send_keys(text)
            self.logger.debug(f"[TYPE] 텍스트 입력 성공: {locator} <- '{text}'")
        except Exception as e:
            self.logger.error(f"[TYPE ERROR] 텍스트 입력 실패: {locator} - {str(e)}")
            raise

    def get_text(self, locator):
        try:
            element = self.wait_for_visible(locator)
            return element.text
        except Exception as e:
            self.logger.error(f"[GET TEXT ERROR] 텍스트 가져오기 실패: {locator} - {str(e)}")
            raise

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
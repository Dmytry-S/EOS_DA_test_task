from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseWebDriver:

    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implisitly_wait(timeout)

    def open_url(self):
        self.browser.get(self.url)

    def find_and_click_button(self, locator_name, locator_value):
        button = self.browser.find_element(locator_name, locator_value)
        button.click()

    def find_and_send_key(self, locator_name, locator_value, text):
        field = self.browser.find_element(locator_name, locator_value)
        field.clear()
        field.send_keys(text)

    def is_element_present(self, locator_name, locator_value, timeout=30):
        try:
            WebDriverWait(self.browser, timeout, 3, TimeoutException). \
                until(EC.presence_of_element_located(locator_name, locator_value))
        except TimeoutException:
            return False
        return True







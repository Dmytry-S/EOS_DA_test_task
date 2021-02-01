from .base_methods import BaseWebDriver
from .locators import LoginPageLocators, MainPageLocators


class LoginPage(BaseWebDriver):

    def should_be_login_page(self):
        self.should_be_login_form()

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Should be login form on the page"

    def enter_login(self):
        self.find_and_send_key(*LoginPageLocators.EMAIL_FIELD, LoginPageLocators.EMAIL_VALUE)

    def enter_password(self):
        self.find_and_send_key(*LoginPageLocators.PASSWORD_FIELD, LoginPageLocators.PASSWORD_VALUE)

    def click_subscribe(self):
        self.find_and_click_button(*LoginPageLocators.BUTTON_LOGIN)

    def is_page_open(self):
        self.is_element_present(*MainPageLocators.MENU_ICON)

    def is_user_correct(self):
        assert self.is_element_correct(*MainPageLocators.USER_VALID), "User is invalid or incorrect"



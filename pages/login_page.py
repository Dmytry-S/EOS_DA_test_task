import time
from .base_methods import BaseWebDriver
from .locators import LoginPageLocators, MainPageLocators


class LoginPage(BaseWebDriver):

    def go_to_login_page(self):
        self.find_and_click_button(*LoginPageLocators.LOGIN_PAGE)

    def should_be_login_page(self):
        # Check if there is a login form on the page available
        self.should_be_login_form()

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def enter_login(self):
        self.find_and_send_key(*LoginPageLocators.EMAIL_FIELD, LoginPageLocators.EMAIL_VALUE)

    def enter_password(self):
        self.find_and_send_key(*LoginPageLocators.PASSWORD_FIELD, LoginPageLocators.PASSWORD_VALUE)

    def click_subscribe(self):
        self.find_and_click_button(*LoginPageLocators.BUTTON_LOGIN)

    def is_page_open(self):
        # To make sure that the page is open, check that there is a button "UPGRADE" on the page available
        self.is_element_present(*MainPageLocators.BUTTON_UPGRADE)

    def is_logged_user_correct(self):
        # To make sure that correct user is logged in, compare user's email to email entered into login form
        self.find_and_click_button(*MainPageLocators.MENU_ICON)
        time.sleep(2)
        self.is_element_text_correct(*MainPageLocators.USER_VALID, LoginPageLocators.EMAIL_VALUE)




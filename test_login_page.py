from pages.locators import LoginPageLocators
from pages.login_page import LoginPage


class TestUserInApp:

    def test_user_login_to_app(self, browser):
        link = LoginPageLocators.URL
        page = LoginPage(browser, link)
        page.open_url()
        page.should_be_login_page()
        page.enter_login()
        page.enter_password()
        page.click_subscribe()
        page.is_page_open()
        page.is_logged_user_correct()

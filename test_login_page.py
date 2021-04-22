from pages.login_page import LoginPage
from pages.environment import PreprodEnv


class TestUserInApp:

    def test_user_login_to_app(self, browser):
        link = PreprodEnv.URL
        page = LoginPage(browser, link)
        page.open_url()
        page.go_to_login_page()
        page.should_be_login_page()
        page.enter_login()
        page.enter_password()
        page.click_subscribe()
        page.is_page_open()
        page.is_logged_user_correct()

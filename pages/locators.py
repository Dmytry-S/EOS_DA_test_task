from selenium.webdriver.common.by import By


class LoginPageLocators:
    URL = "https://preprod.eos.com/crop-monitoring/login/"
    LOGIN_PAGE = (By.TAG_NAME, "[data-id='sign-in-button']")
    LOGIN_FORM = (By.CSS_SELECTOR, ".form-wrap .checked")
    EMAIL_FIELD = (By.ID, "email")
    EMAIL_VALUE = "dmsvtest@gmail.com"
    PASSWORD_FIELD = (By.ID, "password")
    PASSWORD_VALUE = "@2663"
    BUTTON_LOGIN = (By.CSS_SELECTOR, ".submit-btn.primary")


class MainPageLocators:
    BUTTON_UPGRADE = (By.TAG_NAME, "[data-id='upgrade-plan-btn']")
    MENU_ICON = (By.CSS_SELECTOR, ".icon-sb.account-sb.mat-tooltip-trigger")
    USER_VALID = (By.CSS_SELECTOR, ".cdk-overlay-container .email")


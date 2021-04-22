from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_PAGE = (By.TAG_NAME, "[data-id='sign-in-button']")
    LOGIN_FORM = (By.CSS_SELECTOR, ".form-wrap .checked")
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, ".submit-btn.primary")


class MainPageLocators:
    BUTTON_UPGRADE = (By.TAG_NAME, "[data-id='upgrade-plan-btn']")
    MENU_ICON = (By.CSS_SELECTOR, ".icon-sb.account-sb.mat-tooltip-trigger")
    USER_VALID = (By.CSS_SELECTOR, ".cdk-overlay-container .email")


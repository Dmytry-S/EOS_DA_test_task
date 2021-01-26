from selenium.webdriver.common.by import By


class LoginPageLocators:
    URL = "https://preprod.eos.com/crop-monitoring/login/auth"
    EMAIL_FIELD = (By.ID, "email")
    EMAIL_VALUE = "dmsvtest@gmail.com"
    PASSWORD_FIELD = (By.ID, "password")
    PASSWORD_VALUE = "@2663"
    BUTTON_LOGIN = (By.CSS, ".submit-btn.primary")
    MENU_ICON = (By.CSS, ".icon-sb.account-sb.mat-tooltip-trigger")
    USER_VALID = (By.CSS, ".mat-menu-content .email")

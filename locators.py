from selenium.webdriver.common.by import By


class Locators:
    _ENTER_AND_REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    _NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    _EMAIL_INPUT = (By.XPATH, "//input[contains(@name, 'email')]")
    _EMAIL_PASSWORD = (By.XPATH, "//input[contains(@name, 'password')]")
    _REPEAT_PASSWORD = (By.XPATH, "//input[contains(@name, 'submitPassword')]")
    _SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    _USER_AVATAR = (By.XPATH, "//button[contains(@class, 'circleSmall')]")
    _USER_NAME = (By.XPATH, "//h3[contains(@class, 'profileText name')]")
    _ERROR_FIELDS = (By.XPATH, "//div[contains(@class, 'input_inputError')]")
    _ERROR_LABEL = (By.XPATH, "//span[contains(@class, 'input_span') and contains(text(), 'Ошибка')]")
    _LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    _LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    _CREATE_MESSAGE_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    _ALERT = (By.XPATH, "//*[contains(@class, 'popUp_shell')]")
    _NAME = (By.XPATH, "//*[contains(@class, 'createListing_inputRow')]//*[contains(@class, 'input_inputStandart')]")
    _DESCRIPTION = (By.XPATH, "//textarea[contains(@name, 'description')]")
    _PRICE = (By.XPATH, "//input[contains(@name, 'price')]")
    _CATEGORY = (By.XPATH, "//*[contains(@class, 'radioUnput_inputRegular')]")
    _PUBLISH_BUTTON = (By.XPATH, "//button[contains(@type, 'submit')]")
    _ABOUT = (By.XPATH, "//*[contains(@class, 'about')]//h2")


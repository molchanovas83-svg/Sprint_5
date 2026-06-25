from data import Data
from urls import Urls
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestUsersLoginAndLogout:
    def test_login_user(self, driver):
        driver.find_element(*Locators._ENTER_AND_REGISTRATION_BUTTON).click()  # Нажать кнопку "Вход и регистрация"
        driver.find_element(*Locators._EMAIL_INPUT).send_keys(Data.USER_EMAIL)  # Заполнить поле Email
        driver.find_element(*Locators._EMAIL_PASSWORD).send_keys(Data.USER_PASSWORD)  # Заполнить поле Password
        driver.find_element(*Locators._LOGIN_BUTTON).click()  # Нажать кнопку "Войти"
        # Проверить
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators._USER_AVATAR))  # Аватар пользователя
        assert driver.current_url == Urls.LOGIN  # Произошёл переход
        assert driver.find_element(*Locators._USER_NAME).text == Data.USER_NAME  # Отображается имя User

    def test_logout_user(self, driver):
        driver.find_element(*Locators._ENTER_AND_REGISTRATION_BUTTON).click()  # Нажать кнопку "Вход и регистрация"
        driver.find_element(*Locators._EMAIL_INPUT).send_keys(Data.USER_EMAIL)  # Заполнить поле Email
        driver.find_element(*Locators._EMAIL_PASSWORD).send_keys(Data.USER_PASSWORD)  # Заполнить поле Password
        driver.find_element(*Locators._LOGIN_BUTTON).click()  # Нажать кнопку "Войти"
        # Проверить
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators._USER_AVATAR))  # Ожидание
        driver.find_element(*Locators._LOGOUT_BUTTON).click()  # Нажать кнопку "Выйти"
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(Locators._USER_AVATAR))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(Locators._USER_NAME))

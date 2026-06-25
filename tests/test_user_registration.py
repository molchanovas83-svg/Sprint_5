import random
from data import Data
from urls import Urls
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestUsersRegistration:
    def test_user_registration(self, driver):
        driver.find_element(*Locators._ENTER_AND_REGISTRATION_BUTTON).click()  # Нажать кнопку "Вход и регистрация"
        driver.find_element(*Locators._NO_ACCOUNT_BUTTON).click()  # Нажать кнопку "Нет аккаунта"
        driver.find_element(*Locators._EMAIL_INPUT).send_keys(f'mail_{random.randint(100, 999)}@gmail.com')
        driver.find_element(*Locators._EMAIL_PASSWORD).send_keys(Data.USER_PASSWORD)  # Заполнить поле Password
        driver.find_element(*Locators._REPEAT_PASSWORD).send_keys(Data.USER_PASSWORD)  # Повторно заполнить Password
        driver.find_element(*Locators._SUBMIT_BUTTON).click()  # нажать кнопку «Создать аккаунт».
        # Проверить
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators._USER_AVATAR))  # Ожидание
        assert driver.current_url == Urls.REGISTRATION  # произошёл переход
        assert driver.find_element(*Locators._USER_NAME).text == Data.USER_NAME  # Отображается имя User

    def test_user_registration_not_by_mask(self, driver):
        driver.find_element(*Locators._ENTER_AND_REGISTRATION_BUTTON).click()   # Нажать кнопку "Вход и регистрация"
        driver.find_element(*Locators._NO_ACCOUNT_BUTTON).click()  # Нажать кнопку "Нет аккаунта"
        driver.find_element(*Locators._EMAIL_INPUT).send_keys(Data.USER_EMAIL.replace('@', '_'))  # Заполнить поле Email
        driver.find_element(*Locators._SUBMIT_BUTTON).click()  # Нажать кнопку "Создать аккаунт"
        # Проверить
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(Locators._ERROR_FIELDS))  # Ожидание
        assert len(driver.find_elements(*Locators._ERROR_FIELDS)) == 3  # Красным выделено 3 поля
        driver.find_element(*Locators._ERROR_LABEL)  # Отображается сообщение "Ошибка"

    def test_user_registration_existing_user(self, driver):
        driver.find_element(*Locators._ENTER_AND_REGISTRATION_BUTTON).click()   # Нажать кнопку "Вход и регистрация"
        driver.find_element(*Locators._NO_ACCOUNT_BUTTON).click()  # Нажать кнопку "Нет аккаунта"
        driver.find_element(*Locators._EMAIL_INPUT).send_keys(Data.USER_EMAIL)  # Заполнить поле Email
        driver.find_element(*Locators._EMAIL_PASSWORD).send_keys(Data.USER_PASSWORD)  # Заполнить поле Password
        driver.find_element(*Locators._REPEAT_PASSWORD).send_keys(Data.USER_PASSWORD)  # Повторно заполнить Password
        driver.find_element(*Locators._SUBMIT_BUTTON).click()  # Нажать кнопку "Создать аккаунт"
        # Проверить
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(Locators._ERROR_FIELDS))  # Ожидание
        assert len(driver.find_elements(*Locators._ERROR_FIELDS)) == 3  # Красным выделено 3 поля
        driver.find_element(*Locators._ERROR_LABEL)  # Отображается сообщение "Ошибка"


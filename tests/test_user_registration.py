import random
import time
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class TestUsers(Locators):
    def test_user_registration(self, driver):
        driver.find_element(*self._ENTER_AND_REGISTRATION_BUTTON).click()  # Нажать кнопку «Вход и регистрация».
        driver.find_element(*self._NO_ACCOUNT_BUTTON).click()  # Нажать кнопку «Нет аккаунта».
        driver.find_element(*self._EMAIL_INPUT).send_keys('molchanovas83@gmail.com')  # Заполнить поле Email
        driver.find_element(*self._EMAIL_PASSWORD).send_keys('abc123')  # Заполнить поле Password
        driver.find_element(*self._REPEAT_PASSWORD).send_keys('abc123')  # Повторно заполнить поле Password
        driver.find_element(*self._SUBMIT_BUTTON).click()  # нажать кнопку «Создать аккаунт».
        # Проверить
        assert driver.current_url == 'https://qa-desk.education-services.ru/regiatration'  # произошёл переход
        driver.find_element(*self._USER_AVATAR)  # отображается аватар пользователя
        assert driver.find_element(*self._USER_NAME).text == 'User.'  # отображается имя User

    def test_user_registration_not_by_mask(self, driver):
        driver.find_element(*self._ENTER_AND_REGISTRATION_BUTTON).click()   # Нажать кнопку «Вход и регистрация».
        driver.find_element(*self._NO_ACCOUNT_BUTTON).click()  # Нажать кнопку «Нет аккаунта».
        driver.find_element(*self._EMAIL_INPUT).send_keys('molchanovas83_gmail_com')  # Заполнить поле Email
        driver.find_element(*self._SUBMIT_BUTTON).click()  # нажать кнопку «Создать аккаунт».
        # Проверить
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(self._ERROR_FIELDS))  # Ожидание
        assert len(driver.find_elements(*self._ERROR_FIELDS)) == 3  # Красным выделено 3 поля
        driver.find_element(*self._ERROR_LABEL)  # отображается сообщение «Ошибка».

    def test_user_registration_existing_user(self, driver):
        driver.find_element(*self._ENTER_AND_REGISTRATION_BUTTON).click()   # Нажать кнопку «Вход и регистрация».
        driver.find_element(*self._NO_ACCOUNT_BUTTON).click()  # Нажать кнопку «Нет аккаунта».
        driver.find_element(*self._EMAIL_INPUT).send_keys('molchanovas83@gmail.com')  # Заполнить поле Email
        driver.find_element(*self._EMAIL_PASSWORD).send_keys('abc123')  # Заполнить поле Password
        driver.find_element(*self._REPEAT_PASSWORD).send_keys('abc123')  # Повторно заполнить поле Password
        driver.find_element(*self._SUBMIT_BUTTON).click()  # нажать кнопку «Создать аккаунт».
        # Проверить
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(self._ERROR_FIELDS))  # Ожидание
        assert len(driver.find_elements(*self._ERROR_FIELDS)) == 3  # Красным выделено 3 поля
        driver.find_element(*self._ERROR_LABEL)  # отображается сообщение «Ошибка».

    def test_login_user(self, driver):
        driver.find_element(*self._ENTER_AND_REGISTRATION_BUTTON).click()  # Нажать кнопку «Вход и регистрация».
        driver.find_element(*self._EMAIL_INPUT).send_keys('molchanovas83@gmail.com')  # Заполнить поле Email
        driver.find_element(*self._EMAIL_PASSWORD).send_keys('abc123')  # Заполнить поле Password
        driver.find_element(*self._LOGIN_BUTTON).click()  # нажать кнопку «Войти».
        # Проверить
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self._USER_AVATAR))  # аватар пользователя
        assert driver.current_url == 'https://qa-desk.education-services.ru/login'  # произошёл переход
        assert driver.find_element(*self._USER_NAME).text == 'User.'  # отображается имя User

    def test_logout_user(self, driver):
        driver.find_element(*self._ENTER_AND_REGISTRATION_BUTTON).click()  # Нажать кнопку «Вход и регистрация».
        driver.find_element(*self._EMAIL_INPUT).send_keys('molchanovas83@gmail.com')  # Заполнить поле Email
        driver.find_element(*self._EMAIL_PASSWORD).send_keys('abc123')  # Заполнить поле Password
        driver.find_element(*self._LOGIN_BUTTON).click()  # нажать кнопку «Войти».

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self._USER_AVATAR))  # Ожидание
        driver.find_element(*self._LOGOUT_BUTTON).click()  # нажать кнопку «Выйти».
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(self._USER_AVATAR))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(self._USER_NAME))

    def test_create_message_unauthorized_user(self, driver):
        driver.find_element(*self._CREATE_MESSAGE_BUTTON).click()  # Нажать кнопку "Разместить объявление"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self._ALERT))  # Авторизуйтесь

    def test_create_message_authorized_user(self, driver):
        driver.find_element(*self._ENTER_AND_REGISTRATION_BUTTON).click()  # Нажать кнопку «Вход и регистрация».
        driver.find_element(*self._EMAIL_INPUT).send_keys('molchanovas83@gmail.com')  # Заполнить поле Email
        driver.find_element(*self._EMAIL_PASSWORD).send_keys('abc123')  # Заполнить поле Password
        driver.find_element(*self._LOGIN_BUTTON).click()  # нажать кнопку «Войти».

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self._USER_AVATAR))  # Ожидание
        driver.find_element(*self._CREATE_MESSAGE_BUTTON).click()  # Нажать кнопку "Разместить объявление"
        name = f'Товар {random.randint(100, 999)}'
        driver.find_element(*self._NAME).send_keys(name)  # Заполнить «Название»
        driver.find_element(*self._DESCRIPTION).send_keys('Отличный товар!')  # Заполнить «Описание»
        driver.find_element(*self._PRICE).send_keys(500)  # Ввести "Стоимость"
        driver.find_element(*self._CATEGORY).click()  # Выбрать категорию
        driver.find_element(*self._PUBLISH_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self._USER_AVATAR))
        avatar = driver.find_element(*self._USER_AVATAR)
        driver.execute_script('document.body.scrollTop = 0;', avatar)
        time.sleep(1)
        avatar.click()
        assert driver.find_element(*self._ABOUT).text == name  # созданное объявление отображается

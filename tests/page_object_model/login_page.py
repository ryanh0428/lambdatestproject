from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage:
    def __init__(self, driver):
        self.map = LoginPageMap(driver)

    def input_username(self, username: str):
        self.map.username_box().send_keys(username)

    def input_password(self, password: str):
        self.map.password_box().send_keys(password)


class LoginPageMap:
    def __init__(self, driver: webdriver):
        self._driver = driver

    def username_box(self):
        return self._driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']")

    def password_box(self):
        return self._driver.find_element(By.XPATH, "//*[@placeholder='Password']")

    def submit_button(self):
        return self

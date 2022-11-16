import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver


scenarios('../features/login.feature')

login_page = 'https://www.saucedemo.com/'

# Shared Given Steps


@pytest.fixture
def browser():  # replace request with driver to run the test on lambdatest
    # For this example, we will use Firefox
    # You can change this fixture to use other browsers, too.
    # A better practice would be to get browser choice from a config file.
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@given('user is on the sauce demo webpage')
def sauce_demo(browser):
    browser.get(login_page)


@when(parsers.parse('the user type in the user name "{username}" and password "{password}"'))
def user_type_in_info(browser, username, password):
    username_field = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Username']")
    username_field.send_keys(username)
    password_field = browser.find_element(
        By.XPATH, "//*[@placeholder='Password']")
    password_field.send_keys(password)
    browser.find_element(By.ID, "login-button").click()


@then(parsers.parse('the user is directed to inventory page "{inventory_page}"'))
def check_url(browser, inventory_page):

    assert WebDriverWait(browser, 10).until(EC.url_to_be(inventory_page))

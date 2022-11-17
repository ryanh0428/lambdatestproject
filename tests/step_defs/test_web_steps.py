import pytest
import time
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from tests.page_object_model.items_page import Items_page

from tests.page_object_model.login_page import LoginPage


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
    login_page = LoginPage(browser)
    login_page.input_username(username)
    login_page.input_password(password)
    login_page.click_login()


@then(parsers.parse('the user is directed to inventory page "{inventory_page}"'))
def check_url(browser, inventory_page):
    assert inventory_page in browser.current_url


@when('the user click the filter menu on the right hand side')
def click_filter_menu(browser):

    browser.find_element(By.XPATH, "//select").click()


@then(parsers.parse('{option_number} options is avilable to user: "{option1}","{option2}","{option3}","{option4}"'), converters={"option_number": int})
def check_all_options_are_available(browser, option1, option2, option3, option4, option_number):
    items_page = Items_page(browser)

    assert option1 in items_page.list_of_option_text()
    assert option2 in items_page.list_of_option_text()
    assert option3 in items_page.list_of_option_text()
    assert option4 in items_page.list_of_option_text()
    assert len(items_page.list_of_option_text()) == option_number


@when(parsers.parse('the user click the "{option}" option'))
def click_a_filter_option(browser, option):
    items_page = Items_page(browser)
    items_page.select_the_filter_menu(option)


@then('the item will arrange in ascending order')
def check_items_order(browser):
    items_page = Items_page(browser)
    assert items_page.check_items_sorted_by_price()

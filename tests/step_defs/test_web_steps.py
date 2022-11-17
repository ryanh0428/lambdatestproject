

import time
import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium import webdriver
from tests.page_object_model.items_page import Items_page

from tests.page_object_model.login_page import LoginPage


scenarios('../features/login.feature')

login_page = 'https://www.saucedemo.com/'

# Shared Given Steps


# @pytest.mark.usefixtures('driver')
@pytest.fixture
def driver():  # replace request with driver to run the test on lambdatest
    # For this example, we will use Firefox
    # You can change this fixture to use other browsers, too.
    # A better practice would be to get browser choice from a config file.
    dri = webdriver.Chrome()
    dri.implicitly_wait(10)
    yield dri
    dri.quit()


@pytest.fixture
def page_of_items(driver):
    return Items_page(driver)


@given('user is on the sauce demo webpage')
def sauce_demo(driver):
    driver.get(login_page)


@when(parsers.parse('the user type in the user name "{username}" and password "{password}"'))
def user_type_in_info(driver, username, password):
    login_page_object = LoginPage(driver)
    login_page_object.input_username(username)
    login_page_object.input_password(password)
    login_page_object.click_login()


@then(parsers.parse('the user is directed to inventory page "{inventory_page}"'))
def check_url(driver, inventory_page):
    assert inventory_page in driver.current_url


@when('the user click the filter menu on the right hand side')
def click_filter_menu(driver):

    driver.find_element(By.XPATH, "//select").click()


@then(parsers.parse('{option_number} options is avilable to user: "{option1}","{option2}","{option3}","{option4}"'), converters={"option_number": int})
def check_all_options_are_available(driver, option1, option2, option3, option4, option_number):
    items_page = Items_page(driver)

    assert option1 in items_page.list_of_option_text()
    assert option2 in items_page.list_of_option_text()
    assert option3 in items_page.list_of_option_text()
    assert option4 in items_page.list_of_option_text()
    assert len(items_page.list_of_option_text()) == option_number


@when(parsers.parse('the user click the "{option}" option'))
def click_a_filter_option(page_of_items, option):
    page_of_items.select_the_filter_menu(option)


@then('the item will arrange in ascending order')
def check_items_order(page_of_items):
    time.sleep(2)
    assert page_of_items.check_items_sorted_by_price()


# @When('the user pick the first item')
# def pick_the_first_item(browser):


# @Then('the shopping cart showing the number 1')
# @And('the text on the button change to "Remove"')

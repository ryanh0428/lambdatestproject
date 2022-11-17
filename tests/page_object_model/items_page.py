from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Items_page:
    def __init__(self, driver) -> None:
        self.map = Item_page_map(driver)

    def list_of_option_text(self) -> list[str]:
        return [element.text for element in self.map.filter_options()]

    def click_the_filter_menu(self):
        self.map.filter_menu().click()

    def select_the_filter_menu(self, option):
        drop_down_select = Select(self.map.filter_menu())
        drop_down_select.select_by_visible_text(option)

    def check_items_sorted_by_price(self):
        price_list = [float(element.find_element(
            By.CSS_SELECTOR, ".inventory_item_price").text.replace('$', '')) for element in self.map.item_cards()]
        return price_list == sorted(price_list)


class Item_page_map:
    def __init__(self, driver) -> None:
        self._driver = driver

    def filter_menu(self):
        return self._driver.find_element(By.XPATH, "//select")

    def filter_options(self):
        return self._driver.find_elements(By.XPATH, "//option")

    def item_cards(self):
        return self._driver.find_elements(By.XPATH, '//*[@class="inventory_item"]')

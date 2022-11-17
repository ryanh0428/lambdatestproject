from selenium.webdriver.common.by import By


class Items_page:
    def __init__(self, driver) -> None:
        self.map = Item_page_map(driver)

    def list_of_option_text(self) -> list[str]:
        return [element.text for element in self.map.filter_options()]


class Item_page_map:
    def __init__(self, driver) -> None:
        self._driver = driver

    def filter_menu(self):
        return self._driver.find_element(By.XPATH, "//select")

    def filter_options(self):
        return self._driver.find_elements(By.XPATH, "//option")

from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

class InventoryPage(BasePage):
    # Locators
    TITLE = (By.CSS_SELECTOR, "span.title")
    APP_LOGO = (By.CLASS_NAME, "app_logo")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    
    def __init__(self, driver):
        super().__init__(driver)

    def is_inventory_displayed(self):
        is_title_correct = self.is_visible(self.TITLE) and self.get_text(self.TITLE) == "Products"
        is_logo_correct = self.is_visible(self.APP_LOGO) and self.get_text(self.APP_LOGO) == "Swag Labs"
        is_url_correct = "/inventory.html" in self.driver.current_url
        
        return is_title_correct and is_logo_correct and is_url_correct

    def add_item_to_cart(self, item_id):
        # item_id is something like 'add-to-cart-sauce-labs-backpack'
        locator = (By.ID, item_id)
        self.click(locator)

    def remove_item_from_cart(self, item_id):
        # item_id is something like 'remove-sauce-labs-backpack'
        locator = (By.ID, item_id)
        self.click(locator)

    def get_cart_count(self):
        if self.is_visible(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

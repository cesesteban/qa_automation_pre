from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

class BasePage:
    """
    Base Page class that contains common WebDriver methods.
    All Page Objects should inherit from this class.
    """
    
    def __init__(self, driver, base_url=""):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout, ignored_exceptions=[StaleElementReferenceException])

    def open(self, path=""):
        """Navigate to a specific path under the base URL."""
        self.driver.get(f"{self.base_url}{path}")

    def find_element(self, locator):
        """Find an element, wait for it to be visible first."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Wait for an element to be clickable and then click it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    def js_click(self, locator):
        """Use JavaScript click for elements that silently swallow standard clicks in Saucedemo."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text):
        """Wait for an element, clear it, and type the specified text."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator):
        """Return True if element is visible, False otherwise."""
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False

    def get_text(self, locator):
        """Return the text of an element."""
        return self.find_element(locator).text

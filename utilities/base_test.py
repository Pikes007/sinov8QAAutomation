import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:
    """Base class for Selenium test classes."""

    def click_button_by_text(self, button_text):
        """Click a button identified by its visible text.

        Args:
            button_text (str): The visible text of the button to be clicked.
        """
        try:
            button_xpath = f"//button[normalize-space()='{button_text}']" or f"//button@value='{button_text}']" or f"//label[contains(., '{button_text}')]/input[@type='radio' and @value='{button_text}']']"
            button = self.driver.find_element(By.XPATH, button_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            button.click()
            print(f"Clicked on button with text: {button_text}")
        except NoSuchElementException as e:
            print(f"Button with text '{button_text}' not found", str(e))

    def get_text_of_element(self, locator):
        """Get the text content of a web element.

        Args:
            locator (tuple): A tuple representing the locator strategy and value.

        Returns:
            str: The text content of the located web element.
        """
        element = self.driver.find_element(*locator)
        element_text = element.text
        print("Element text: ", element_text)
        return element_text

    def take_screenshot(self, filename):
        """Capture a screenshot of the current browser window.

        Args:
            filename (str): The filename for the saved screenshot.
        """
        self.driver.get_screenshot_as_file(filename)

    def hover_on_element(self, element, max_retries=5):
        """Hover over a web element.

        Args:
            element (tuple): A tuple representing the locator strategy and value.
            max_retries (int, optional): The maximum number of retries in case of timeout. Defaults to 5.
        """
        wait = WebDriverWait(self.driver, 10)

        for _ in range(max_retries):
            try:
                hover = wait.until(EC.visibility_of_element_located(element))
                is_displayed = hover.is_displayed()

                if is_displayed:
                    time.sleep(1)
                    actions = ActionChains(self.driver)
                    actions.move_to_element(hover).perform()
                    return
            except TimeoutException:
                print("Element not displayed within the specified timeout.")

        print(f"Element not displayed within the specified timeout. Retrying...")



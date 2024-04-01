from typing import List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import NoSuchElementException
import logging


logger = logging.getLogger('selenium')
logger.setLevel(logging.INFO)

class Base:
    def __init__(self, driver: WebDriver):
        self._driver = driver
    
    def _open_url(self, url: str):
        self._driver.get(url)
    
    def _find(self, locator: tuple)  -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 5):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)
    
    def _click(self, locator: tuple, time: int = 5):
        self._wait_until_element_is_clickable(locator, time)
        self._find(locator).click()
    
    def _clear(self, locator: tuple, time: int = 5):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).clear()

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 15):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))
    
    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 5):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))
    
    def _wait_until_element_is_not_visible(self, locator: tuple, time: int = 5):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.invisibility_of_element(locator))
    
    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 5):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    def _get_text(self, locator: tuple, time: int = 5) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text    
    
    def _get_table_elements(self, locator1, locator2, time: int = 15) -> List[WebElement]:
        # self._wait_until_element_is_visible(locator, time)
        wait = WebDriverWait(self._driver,time)
        wait.until(ec.visibility_of_any_elements_located(locator1))
        elements = self._driver.locate_with(locator1).below(locator2)
        print(elements)
        return elements

    
    @property
    def current_url(self) -> str:
        return self._driver.current_url
    
    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False
    
    


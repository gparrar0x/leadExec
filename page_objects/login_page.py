from page_objects.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class LoginPage(Base):
    __url = "https://leadexec.clickpointsoftware.com/Account/Login"
    __username_field = (By.ID, "Username")
    __password_field = (By.ID, "Password")
    __submit_button = (By.ID, "loginBtn")

    
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    
    def open(self):
        super()._open_url(self.__url)
    
    def execute_login(self, username, password):
        super()._type(self.__username_field,username)
        super()._type(self.__password_field,password)
        super()._click(self.__submit_button)
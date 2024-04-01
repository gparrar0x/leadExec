from page_objects.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LeadSourcePage(Base):
    __url = "https://leadexec.clickpointsoftware.com/LeadSources/List"
    __navBar_button = (By.ID, "navItem_6")
    __create_button = (By.ID, "createLeadSourceBtn")
    __open_button = (By.ID, "btnOpen")
    __source_name = (By.ID, "Name")
    __campaign_name = (By.ID, "CampaignDetails_GeneralOptions_Name")
    __next_button = (By.ID, "createNextBtn")
    __createSource_button = (By.ID, "createSourceBtn")
    __success_message = (By.XPATH, '//*[@id="leadSourceWelcomeDialog"]/div/div/div[2]/h3')
    __close_button = (By.XPATH, '//*[@id="leadSourceWelcomeDialog"]/div/div/div[3]/button')
    __save_changes_button = (By.ID, "btnSave")
    __sort_by_name_button = (By.XPATH, '//*[@id="dx-col-5"]/div[1]')
    __first_row = (By.CSS_SELECTOR, 'tr[aria-rowindex="1"]')
    __deleteSource_button = (By.ID, "btnDelete")
    __delete_confirmation_button = (By.ID, "confirmationButton")
    __notification_message_body = (By.ID, "NotiflixNotifyWrap")
    __notification_message_text = (By.XPATH, '//*[@id="NotiflixNotify-1"]/span')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    
    def open(self, time: int = 10):
        super()._click(self.__navBar_button,time)
    
    def message_verification(self,time: int = 5):
        super()._wait_until_element_is_visible(self.__notification_message_body, time)
        return super()._get_text(self.__notification_message_text, time)
    
    def create_new_source(self, source_name, campaign_name, time: int = 15):
        super()._click(self.__create_button,time)
        super()._type(self.__source_name, source_name,time)
        super()._click(self.__next_button,time)
        super()._type(self.__campaign_name,campaign_name,time)
        super()._click(self.__next_button,time)
        super()._click(self.__createSource_button,time)
        super()._wait_until_element_is_visible(self.__success_message, time)
        success_msg = super()._get_text(self.__success_message, time)
        super()._click(self.__close_button, time)
        super()._click(self.__save_changes_button, time)
        return success_msg
    
    def open_first_source(self, time:int = 15):
        super()._click(self.__first_row, time)
        super()._click(self.__open_button, time)

    def delete_first_source(self, time: int = 15):
        super()._click(self.__first_row)
        super()._click(self.__deleteSource_button)
        super()._click(self.__delete_confirmation_button)
    
    @property
    def expected_url(self) -> str:
        return self.__url
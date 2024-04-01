from page_objects.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CampaignsPage(Base):
    __url = "https://leadexec.clickpointsoftware.com/LeadSources/Campaigns"
    __navBar_button = (By.ID, "navItem_7")
    __create_button = (By.ID, "btnCreateCampaign")
    __campaign_name = (By.ID, "Create_GeneralOptions_Name")
    __next_button = (By.ID, "createNextBtn")
    __createCampaign_button = (By.ID, "createSourceCampaignBtn")
    __campaignSave_button = (By.ID, "btnCampaignSave")
    __table = (By.CLASS_NAME, "dx-row dx-datagrid-filter-row")
    __table_column = (By.CSS_SELECTOR, 'td[aria-colindex="6"]')
    __open_button = (By.ID, "btnOpenCampaign")
    __sort_by_name_button = (By.XPATH, '//*[@id="dx-col-5"]/div[1]')
    __first_row = (By.CSS_SELECTOR, 'tr[aria-rowindex="1"]')
    __deleteCampaign_button = (By.ID, "btnDelete")
    __delete_confirmation_button = (By.ID, "confirmationButton")
    __notification_message_body = (By.ID, "NotiflixNotifyWrap")
    __notification_message_text = (By.XPATH, '//*[@id="NotiflixNotify-4"]/span')
    __general_settings_panel  = (By.ID, "generalSettingsPanel")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    
    def open(self, time: int = 10):
        super()._click(self.__navBar_button,time)
    
    def create_new_campaign(self, campaign_name, time: int = 5):
        super()._click(self.__create_button)
        super()._type(self.__campaign_name,campaign_name)
        super()._click(self.__next_button)
        super()._click(self.__next_button)
        super()._click(self.__next_button)
        super()._click(self.__next_button)
        super()._click(self.__createCampaign_button)
        super()._click(self.__campaignSave_button)
    
    def open_first_campaign(self, time:int = 5):
        super()._click(self.__first_row)
        super()._click(self.__open_button)
        super()._wait_until_element_is_visible(self.__general_settings_panel)

    def delete_first_campaign(self, time: int = 15):
        super()._click(self.__first_row)
        super()._click(self.__deleteCampaign_button)
        super()._click(self.__delete_confirmation_button)
    
    def message_verification(self,time: int = 5):
        super()._wait_until_element_is_visible(self.__notification_message_body, time)
        return super()._get_text(self.__notification_message_text, time)

    def sort_list_by_name(self):
        super()._click(self.__sort_by_name_button)
    
    def get_table_elements(self):
        elements = super()._get_table_elements(self.__table,self.__table_column)
        print(elements)
        return elements

    @property
    def expected_url(self) -> str:
        return self.__url
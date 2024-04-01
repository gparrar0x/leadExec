from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from page_objects.login_page import LoginPage
from page_objects.campaigns_page import CampaignsPage
import pytest

campaign_name = "Selenium Campaign Test"
username = "gparrar@pm.me"
passw = "5737b3f!"

class TestCampaigns:
    def test_Toolbar_Create_Campaign(self, driver):
        login_page = LoginPage(driver)
        campaigns_page = CampaignsPage(driver)

        login_page.open()
        login_page.execute_login(username,passw)
        campaigns_page.open()
        assert campaigns_page.expected_url == campaigns_page.current_url
        campaigns_page.create_new_campaign(campaign_name)
        assert campaigns_page.message_verification() == "Created"
    
    def test_Toolbar_Delete_Campaign(self, driver):
        login_page = LoginPage(driver)
        campaigns_page = CampaignsPage(driver)

        login_page.open()
        login_page.execute_login(username, passw)
        campaigns_page.open()
        assert campaigns_page.expected_url == campaigns_page.current_url
        campaigns_page.delete_first_campaign()

    def test_Toolbar_Open_Campaign(self, driver):
        login_page = LoginPage(driver)
        campaigns_page = CampaignsPage(driver)

        login_page.open()
        login_page.execute_login(username, passw)
        campaigns_page.open()
        assert campaigns_page.expected_url == campaigns_page.current_url
        campaigns_page.open_first_campaign()
        assert campaigns_page.message_verification() == "Selected items have been removed"

    
    # def test_Grid_Sorting(self, driver):
    #     login_page = LoginPage(driver)
    #     campaigns_page = CampaignsPage(driver)
        
    #     login_page.open()
    #     login_page.execute_login(username, passw)
        
    #     campaigns_page.open()
    #     unsorted_grid = campaigns_page.get_table_elements()
    #     campaigns_page.sort_list_by_name()
    #     sorted_grid = campaigns_page.get_table_elements()
    #     sorted_list = sorted(unsorted_grid,key=str.lower)
    #     for i in sorted_grid:
    #         assert sorted_grid[i] == sorted_list[i]


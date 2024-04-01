from page_objects.login_page import LoginPage
from page_objects.lead_sources_page import LeadSourcePage

username = "gparrar@pm.me"
passw = "5737b3f!"
source_name = "Source Test"
campaign_name = "Campaign Test"

class TestSources:
    def test_Toolbar_Create_Source(self, driver):
        login_page = LoginPage(driver)
        source_page = LeadSourcePage(driver)

        login_page.open()
        login_page.execute_login(username, passw)
        source_page.open()
        assert source_page.expected_url == source_page.current_url
        msg = source_page.create_new_source(source_name, campaign_name)
        assert msg == "Your lead source has been created!"
    
    def test_Toolbar_Open_Source(self, driver):
        login_page = LoginPage(driver)
        source_page = LeadSourcePage(driver)

        login_page.open()
        login_page.execute_login(username, passw)
        source_page.open()
        assert source_page.expected_url == source_page.current_url
        source_page.open_first_source()
        assert "https://leadexec.clickpointsoftware.com/LeadSources/Detail/" in source_page.current_url


    def test_Toolbar_Delete_Source(self, driver):
        login_page = LoginPage(driver)
        source_page = LeadSourcePage(driver)

        login_page.open()
        login_page.execute_login(username, passw)
        source_page.open()
        assert source_page.expected_url == source_page.current_url
        source_page.delete_first_source()
        assert source_page.message_verification() == "Selected items have been removed"

''' TO DO:
- Improve Login Procedure
- Assert creation/edition/deletion of entities using API
- Improve with Data Driven Testing using a controled data set for all inputs

'''
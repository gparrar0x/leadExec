import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager



#@pytest.fixture(params=["chrome", "firefox"])
@pytest.fixture()
def driver(request): 
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver")
    if browser == "chrome":
        options = Options()
        options.add_argument('--start-maximized')
        options.add_argument('--disk-cache-dir=cache')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-notifications')
        options.page_load_strategy = 'eager'
        my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Got {browser}, chrome or firefox expected")
    #my_driver.implicitly_wait(20)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)")

import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

#pytest_addoption 用來為命令行選項 --browser 設定默認值、說明文字，並告訴 pytest 如何處理這個選項。
def pytest_addoption(parser):
    parser.addoption("--browser", action= "store", default= "chrome", help= "Specify the browser: chrome or firefox or edge")

#request.config.getoption("--browser") 會取得命令行選項 --browser 的值
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
    elif browser == "edge":
        driver = webdriver.Edge()
        driver.implicitly_wait(10)
    elif browser == "safari":
        driver = webdriver.Safari()
        driver.implicitly_wait(10)
    else:
        raise ValueError("Unsup browser")

    yield driver
    driver.quit()

################ for pytest html reports #############
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = "Test Saucedemo Login"
    config.stash[metadata_key]['Test Modules Name'] = "Admin Login Tests"
    config.stash[metadata_key]['Tester Name'] = "Nomik"

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
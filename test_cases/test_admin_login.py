import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker

class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_Maker.log_gen()

    def test_title_verification(self, setup):
        self.logger.info("*************Test_01_Admin_Login*************")
        self.logger.info("*************verification of admin login page title*************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "Swag Labs"

        if act_title == exp_title:
            self.logger.info("*************test_title_verification title matched*************")
            assert True
        else:
            self.driver.save_screenshot("./screenshots/test_title_verification.png")
            self.logger.info("*************test_title_verification title not matched*************")
            assert False

    def test_valid_admin_login(self, setup):
        self.logger.info("*************test_valid_admin_login started*************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_page_lp = Login_Admin_Page(self.driver)
        self.admin_page_lp.enter_username(self.username)
        self.admin_page_lp.enter_password(self.password)
        self.admin_page_lp.click_login()
        act_dashobard_text = self.driver.find_element(By.XPATH, "//*[@id='header_container']/div[1]/div[2]/div").text

        if act_dashobard_text == "Swag Labs":
            self.logger.info("*************dashobard text found*************")
            assert True
        else:
            self.driver.save_screenshot("./screenshots/test_valid_admin_login.png")
            assert False

    def test_invalid_admin_login(self, setup):
        self.logger.info("*************test_invalid_admin_login started*************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_page_lp = Login_Admin_Page(self.driver)
        self.admin_page_lp.enter_username(self.invalid_username)
        self.admin_page_lp.enter_password(self.password)
        self.admin_page_lp.click_login()
        self.driver.implicitly_wait(10)
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h3[data-test="error"]'))
        )

        if error_message.text == "Epic sadface: Username and password do not match any user in this service":
            self.logger.info("*************test_invalid_admin_login error messages matched*************")
            assert True
        else:
            self.driver.save_screenshot("./screenshots/test_invalid_admin_login.png")
            assert False
import time

import webutils as webutils
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from V2.base.base_analyze import get_json
from V2.page.login_page import *
from V2.util.pyalish import Webutils
import pytest



class TestLogin():

    def setup(self):
        self.driver = Webutils.web_driver()
        self.login_page = Login_Page(self.driver)
        self.driver.implicitly_wait(10)
        self.driver.get("http://192.168.2.144/")

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("params", get_json())
    def test_click_login_link(self, params):
        self.login_page.click_login_link()
        self.login_page.input_user_name(params["username"])
        self.login_page.input_pass_word(params["password"])
        self.login_page.input_verfiy_code(params["modifycode"])
        self.login_page.click_sure_tag()
        time.sleep(5)
        element = self.login_page.back_mag()
        print(element)
        assert '账号不存在!' == element



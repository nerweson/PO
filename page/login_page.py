from selenium import webdriver
from selenium.webdriver.common.by import By

from V2.base.base_action import Base_Action

login_link = By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/a[1]'
input_user_element = By.XPATH, '//*[@id="username"]'
input_paw_element = By.XPATH, '//*[@id="password"]'
verfiy_code_element = By.XPATH, '//*[@id="verify_code"]'
click_tag_element = By.XPATH, '//*[@id="loginform"]/div/div[6]/a'
mas = By.XPATH, '//*[@id="layui-layer1"]/div[2]'
class Login_Page(Base_Action):

    def click_login_link(self):

        return self.click(login_link)

    def input_user_name(self, value):

        return self.find_ele1(input_user_element).send_keys(value)

    def input_pass_word(self, value):

        return self.find_ele2(input_paw_element).send_keys(value)

    def input_verfiy_code(self, value):

        return self.find_ele3(verfiy_code_element).send_keys(value)

    def click_sure_tag(self):

        return self.click(click_tag_element)

    def back_mag(self):

        return self.find_ele2(mas).text

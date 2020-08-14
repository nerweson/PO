from selenium import webdriver


class Webutils:

    @classmethod
    def web_driver(cls):
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver

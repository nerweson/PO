

class Base_Action():
    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        return self.driver.find_element_by_xpath(element[1]).click()

    def find_ele1(self, element):
        return self.driver.find_element_by_xpath(element[1])

    def find_ele2(self, element):

        return self.driver.find_element_by_xpath(element[1])

    def find_ele3(self, element):

        return self.driver.find_element_by_xpath(element[1])

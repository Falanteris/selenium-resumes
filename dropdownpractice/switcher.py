from selenium.webdriver.common.by import By


class Switcher():
    to_round = (By.ID,"ctl00_mainContent_rbtnl_Trip_1")
    to_one_way = (By.ID, "ctl00_mainContent_rbtnl_Trip_0")
    to_multi = (By.ID, "ctl00_mainContent_rbtnl_Trip_2")
    def __init__(self,driver):
        self.driver = driver

    def switch_to_round(self):
        self.driver.find_element(*Switcher.to_round).click()
        return self.driver

    def switch_to_multi(self):
        self.driver.find_element(*Switcher.to_multi).click()
        return self.driver

    def switch_to_one_way(self):
        self.driver.find_element(*Switcher.to_one_way).click()
        return self.driver
from selenium.webdriver.common.by import By

from dvwautomation.DvwaCookieManager import DvwaCookie


class LoginDvwa(DvwaCookie):
    username = (By.NAME,"username")
    password = (By.NAME, "password")
    login_button = (By.NAME,"Login")

    def __init__(self,driver,logger):
        DvwaCookie.__init__(self,"login.pkl",driver,logger)

    def login(self,username,password):
        self.driver.find_element(*LoginDvwa.username).send_keys(username)
        self.driver.find_element(*LoginDvwa.password).send_keys(password)
        self.driver.find_element(*LoginDvwa.login_button).click()
        self.save_cookie()
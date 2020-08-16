from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from testwisely.Switcher import Switcher


class PopupWindow(Switcher):
    link_locator = (By.PARTIAL_LINK_TEXT,"Popup")
    buy_now_button = (By.ID,"buy_now_btn")
    main_title = (By.XPATH,'//h4[text()="TestWise Demo Page"]')

    def __init__(self,driver,logger):
        Switcher.__init__(self,driver,logger)

    def run(self,action):
        # action is 'accept' or 'dismiss'
        self.driver.implicitly_wait(10)
        self.switch(PopupWindow.link_locator,self.operations,action)
    def operations(self,*args):
        button = self.driver.find_element(*PopupWindow.buy_now_button)
        button.click()
        alert = self.driver.switch_to.alert
        self.logger.info(alert.text)
        if args[0] == "accept":
            alert.accept()
            waiter = WebDriverWait(self.driver,10)
            try:
                waiter.until(EC.presence_of_element_located(PopupWindow.main_title))
                self.logger.info("Popup testing.. finished")
            except Exception as e:
                self.logger.error("Popup testing.. failed")
                raise Exception(e)
        else:
            alert.dismiss()

        pass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from testwisely.Switcher import Switcher


class HandleIframes(Switcher):
    partial_link = (By.PARTIAL_LINK_TEXT,"iframes")
    frame_2 = (By.ID,"Frame2")
    frame_1 = (By.ID, "Frame1")
    error_div = (By.CSS_SELECTOR,"div[class=error-v1]")
    error_message = (By.TAG_NAME,"*")
    def __init__(self,driver,logger):
        Switcher.__init__(self,driver,logger)

    def run(self):
        self.switch(HandleIframes.partial_link,self.iframe_operations)
        pass
    def iframe_operations(self,*args):
        # frame 1
        frame_1 = self.driver.find_element(*HandleIframes.frame_1)
        self.driver.switch_to.frame(frame_1)
        error_div = self.driver.find_element(*HandleIframes.error_div)
        errors = error_div.find_elements(*HandleIframes.error_message)
        for error in errors:
            self.logger.info("Found error on page on Frame 1 : {}".format(error.text))
        self.driver.switch_to.default_content()
        # frame 2
        frame_2 = self.driver.find_element(*HandleIframes.frame_2)
        self.driver.switch_to.frame(frame_2)
        error_div = self.driver.find_element(*HandleIframes.error_div)
        errors = error_div.find_elements(*HandleIframes.error_message)
        for error in errors:
            self.logger.info("Found error on page on Frame 2 : {}".format(error.text))
        self.driver.switch_to.default_content()
        pass
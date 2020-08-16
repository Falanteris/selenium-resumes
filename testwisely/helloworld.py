from selenium.webdriver.common.by import By

from testwisely.Switcher import Switcher
from utilities.LogFormatClass import LogFormatClass


class HelloWorld(Switcher):
    body = (By.ID, "body")
    partial_link = (By.PARTIAL_LINK_TEXT,"Hello World")
    wonderful = (By.XPATH,"div/p/strong")
    def __init__(self,driver,logger):
        Switcher.__init__(self,driver,logger)
    def run(self):

        self.switch(HelloWorld.partial_link,self.hello_world_operation)

    def hello_world_operation(self,*args):
        content = self.driver.find_element(*HelloWorld.body)
        self.logger.info(content.text)
        self.logger.info(content.find_element(*HelloWorld.wonderful).text)



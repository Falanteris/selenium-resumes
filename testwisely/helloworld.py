from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from testwisely.Switcher import Switcher
from utilities.LogFormatClass import LogFormatClass


class HelloWorld(Switcher):
    body = (By.ID, "body")
    partial_link = (By.PARTIAL_LINK_TEXT,"Hello World")
    wonderful = (By.XPATH,"div/p/strong")
    def __init__(self,driver,logger):
        Switcher.__init__(self,driver,logger)
    def run(self):
        self.driver.implicitly_wait(10)
        self.switch(HelloWorld.partial_link,self.hello_world_operation)

    def hello_world_operation(self,*args):
        waiter = WebDriverWait(self.driver,10)
        content = waiter.until(EC.presence_of_element_located(HelloWorld.body))
        # content = self.driver.find_element(*HelloWorld.body)
        self.logger.info(content.text)
        self.logger.info(content.find_element(*HelloWorld.wonderful).text)



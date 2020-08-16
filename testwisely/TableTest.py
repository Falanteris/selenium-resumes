from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from testwisely.Switcher import Switcher


class TableHandle(Switcher):
    link_locator = (By.PARTIAL_LINK_TEXT,"Event")
    table_data_locator = "//td[contains(text(),{})]/parent::tr/td"
    table_header_locator = (By.XPATH,"//th[contains(text(),'Received date')]/parent::tr/th")
    link_data = (By.TAG_NAME,"a")
    h1_title = (By.TAG_NAME,"h1")
    def __init__(self,driver,logger):
        Switcher.__init__(self, driver,logger)

    def run(self,issue):
        self.driver.implicitly_wait(10)
        self.switch(TableHandle.link_locator,self.operations,issue)
        pass

    def operations(self,*args):
        issue = args[0]
        waiter = WebDriverWait(self.driver, 10)
        table_data_locator = (By.XPATH, TableHandle.table_data_locator.format(issue))
        table_data = self.driver.find_elements(*table_data_locator)
        headers = [data.text for data in self.driver.find_elements(*TableHandle.table_header_locator)]

        for items in table_data:
            self.logger.info("{} = {}".format(headers[table_data.index(items)],items.text))
        table_data[0].find_element(*TableHandle.link_data).click()

        h1 = waiter.until(EC.presence_of_element_located(TableHandle.h1_title))
        self.logger.debug("Acquired text = {}".format(h1.text))
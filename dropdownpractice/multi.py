from selenium.webdriver.common.by import By

from dropdownpractice.flight import FlightHandler

class MultiHandler(FlightHandler):

    multi_item_xpath = (By.XPATH,"//div[contains(@id,'marketCityPair')]")
    add_more = (By.ID,"btnAddMore1")
    Popup = (By.ID,"MultiCityModelAlert")
    ExtraRows = (By.CLASS_NAME,"rowTripPlanner")
    def __init__(self,driver,logger):
        FlightHandler.__init__(self,driver,logger)
        self.driver.find_element(*MultiHandler.Popup).click()
        self.rows = []
        self.driver.implicitly_wait(3)
        self.fetch_rows()
    def fetch_rows(self):
        self.rows.append(self.driver.find_element(*MultiHandler.multi_item_xpath))
        for items in self.driver.find_elements(*MultiHandler.ExtraRows):
            self.rows.append(items)
    def add_rows(self):
        self.driver.find_element(*MultiHandler.add_more).click()
        self.rows = self.driver.find_elements(*MultiHandler.multi_item_xpath)
    def get_row_length(self):
        return len(self.rows)
    def set_focused_row(self,idx):
        focus = self.driver.find_elements(*MultiHandler.multi_item_xpath)
        self.root_driver = self.driver
        self.driver = focus[idx]

    def return_back(self):
        self.driver = self.root_driver



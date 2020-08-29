from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains as AC
from dropdownpractice.flight import FlightHandler


class RoundTripHandler(FlightHandler):
    CalendarTrigger1 = (By.ID, "ctl00_mainContent_view_date1")
    CalendarTrigger = (By.ID, "ctl00_mainContent_view_date2")
    MayDatesSelector = "//*[@data-handler='selectDay' and @data-month='4']/a[text()='{}']"
    JuneDatesSelector = "//*[@data-handler='selectDay' and @data-month='4']/a[text()='{}']"
    Body = (By.ID,"flightSearchContainer")
    def dismiss_depart_date(self):
        ac = AC(self.driver)
        ac.move_to_element(self.driver.find_element(*RoundTripHandler.Body)).click().perform()
        #self.driver.find_element(*RoundTripHandler.Body).click()

    def __init__(self,driver,logger):
        FlightHandler.__init__(self,driver,logger)

    def select_date(self,month,date):
        #self.driver.find_element(*RoundTripHandler.Body).click()
        self.driver.find_element(*RoundTripHandler.CalendarTrigger).click()

        opts = {
            "4":RoundTripHandler.MayDatesSelector,
            "5":RoundTripHandler.JuneDatesSelector
        }
        locator = (By.XPATH,opts.get(month).format(date))
        self.driver.find_element(*locator).click()

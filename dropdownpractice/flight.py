
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class FlightHandler(BaseClass):
    From = (By.ID, "ctl00_mainContent_ddl_originStation1_CTXT")
    FromXPATH = (By.XPATH,"//*[contains(@id,'mainContent_ddl_originStation') and contains(@id,'CTXT')]")
    ToXPATH = (By.XPATH, "//*[contains(@id,'mainContent_ddl_destinationStation') and contains(@id,'CTXT')]")
    To = (By.ID, "ctl00_mainContent_ddl_destinationStation1_CTXT")
    ParentTrigger = (By.ID,"divAdult")
    ChildTrigger = (By.ID,"divChild")
    InfantTrigger = (By.ID, "divInfant")
    PAX = (By.ID, "divpaxinfo")
    PassengerDivLocator = "//div[@class='ad-row-left']/label[@class='guestlbl' and contains(text(),'{}')]"
    IncrDecrButtonLocator = (By.XPATH,"//div[@class='ad-row-right']")
    GroupSelector = "//div[contains(@id,'dropdownGroup')]/h3[text()='{}']/parent::div/div[@class ='dropdownDiv']/ul/li/a[contains(text(),'{}')]"
    CurrencySelector = (By.NAME, "ctl00$mainContent$DropDownListCurrency")
    FamilyAndFriendsChecklist = (By.NAME,"ctl00$mainContent$chk_friendsandfamily")
    MinorCheckList = (By.NAME,"ctl00$mainContent$chk_Unmr")
    PlusMinus={
    "Adult" : {
        "Plus" : (By.ID,"hrefIncAdt"),
        "Minus" : (By.ID,"hrefDecAdt")
    },
    "Child" : {
        "Plus": (By.ID, "hrefIncChd"),
        "Minus": (By.ID, "hrefDecChd")

    },
        "Infant": {
            "Plus": (By.ID, "hrefIncInf"),
            "Minus": (By.ID, "hrefDecInf")

        }
    }
    ConfirmPax = (By.ID, "btnclosepaxoption")
    Confirm = (By.NAME,"ctl00$mainContent$btn_FindFlights")
    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger
        self.pax = False
        self.driver.implicitly_wait(5)
    def set_check_list(self,special):
        family_and_friends = self.driver.find_element(*FlightHandler.FamilyAndFriendsChecklist)
        minor = self.driver.find_element(*FlightHandler.MinorCheckList)
        if special == "Minor":
            minor.click()
        else:
            family_and_friends.click()
    def set_currency(self,currency):
        selector = self.driver.find_element(*FlightHandler.CurrencySelector)
        self.select(selector,currency)
    def set_from(self,region,location):
        src = self.driver.find_element(*FlightHandler.FromXPATH)
        src.click()
        generate_parent_locator = (By.XPATH, FlightHandler.GroupSelector.format(region, location))
        locator = src.find_elements(*generate_parent_locator)
        locator[0].click()

        pass

    def set_to(self,region,location):
        src = self.driver.find_element(*FlightHandler.ToXPATH)
        generate_parent_locator = (By.XPATH, FlightHandler.GroupSelector.format(region,location))
        locator = src.find_elements(*generate_parent_locator)
        locator[1].click()
        pass
    def configure_pax(self):
        self.driver.find_element(*FlightHandler.PAX).click()
    def get_buttons(self,age):
        #
        # generated_locator = (By.XPATH,FlightHandler.PassengerDivLocator.format(age))
        #
        # # self.wait_for_presence(generated_locator,10)
        # # div = self.driver.find_element(*generated_locator)
        # # div.click()
        self.plus = self.driver.find_element(*FlightHandler.PlusMinus[age]["Plus"])
        self.minus = self.driver.find_element(*FlightHandler.PlusMinus[age]["Minus"])

        # click()
        # button_group.find_element(*FlightHandler.Minus).clck()
    def add_current_type(self):
        self.plus.click()
    def subtract_current_type(self):
        self.minus.click()
    def commit_pax(self):
        self.driver.find_element(*FlightHandler.ConfirmPax).click()


    def book(self):
        self.driver.find_element(*FlightHandler.Confirm).click()
    def handle_alert(self):
        try:
            alert = self.driver.switch_to.alert
            self.logger.error(alert.text)
            alert.accept()
        except Exception as e:
            self.logger.info("No errors were present..")
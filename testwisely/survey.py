from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from testwisely.Switcher import Switcher


class SurveyHandler(Switcher):
    partial_link = (By.PARTIAL_LINK_TEXT,"Survey")
    select_items = (By.ID,"your_role")
    radio_roles = (By.NAME,"role")
    radio_regression = (By.NAME,"run_regression_tests")
    get_checkboxes = (By.CSS_SELECTOR,"input[type='checkbox']")
    text_area = (By.ID,"reason_txt")
    submit = (By.XPATH,"//input[@value='Show Solution']")
    solution = (By.ID,"solution")
    def __init__(self,driver,logger):
        Switcher.__init__(self,driver,logger)

    def run(self,role, percentage, freq, challenges, comment):
        self.switch(SurveyHandler.partial_link, self.survey_operations, role, percentage, freq, challenges, comment )
        pass
    def survey_operations(self,*args):
        # question 1
        options = Select(self.driver.find_element(*SurveyHandler.select_items)).options
        for option in options:
            if option.text == args[0]:
                option.click()
                break
        self.logger.info("You have chosen : {}".format(args[0]))
        # question 2
        choices = self.driver.find_elements(*SurveyHandler.radio_roles)
        for choice in choices:
            if choice.get_attribute("value") == args[1]:
                choice.click()
                break
        self.logger.info("You have chosen : {}".format(args[1]))
        # question 3
        choices = self.driver.find_elements(*SurveyHandler.radio_regression)
        for choice in choices:
            if choice.get_attribute("value") == args[2]:
                choice.click()
                break
        self.logger.info("You have chosen : {}".format(args[2]))
        # question 4
        choices = self.driver.find_elements(*SurveyHandler.get_checkboxes)
        for choice in choices:
            if choice.get_attribute("name") in args[3]:
                choice.click()
        self.logger.info("You have chosen : {}".format(args[3]))
        # question 5
        input_box = self.driver.find_element(*SurveyHandler.text_area)
        input_box.send_keys(args[4])
        self.logger.info("You have written : {}".format(args[4]))

        self.driver.find_element(*SurveyHandler.submit).click()

        self.logger.info(self.driver.find_element(*SurveyHandler.solution).text)
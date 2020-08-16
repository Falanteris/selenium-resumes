from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from testwisely.Switcher import Switcher


class PageSameLink(Switcher):
    link_locator = (By.PARTIAL_LINK_TEXT,"Customer")
    show_answer_1 = (By.XPATH,"//a[@onclick='show_answer_1();']")
    show_answer_2 = (By.XPATH, "//a[@onclick='show_answer_2();']")
    show_answer_3 = (By.XPATH, "//a[@onclick='show_answer_3();']")
    get_answer_1 = (By.ID,"answer1")
    get_answer_2 = (By.ID, "answer2")
    get_answer_3 = (By.ID, "answer3")

    def __init__(self,driver,logger):
        Switcher.__init__(self,driver,logger)
    def run(self):
        self.driver.implicitly_wait(10)
        self.switch(PageSameLink.link_locator,self.operations)
        pass
    def operations(self):

        self.driver.execute_script('show_answer_1 = ()=>{document.getElementById(arguments[0]).style=""}',
                                   PageSameLink.get_answer_1[1])
        self.driver.execute_script('show_answer_2 = ()=>{document.getElementById(arguments[0]).style=""}',
                                   PageSameLink.get_answer_2[1])
        self.driver.execute_script('show_answer_3 = ()=>{document.getElementById(arguments[0]).style=""}',
                                   PageSameLink.get_answer_3[1])
        self.driver.find_element(*PageSameLink.show_answer_1).click()
        self.driver.find_element(*PageSameLink.show_answer_2).click()
        self.driver.find_element(*PageSameLink.show_answer_3).click()
        self.logger.info("Answer 1 : {}".format(self.driver.find_element(*PageSameLink.get_answer_1).text))
        self.logger.info("Answer 2 : {}".format(self.driver.find_element(*PageSameLink.get_answer_2).text))
        self.logger.info("Answer 3 : {}".format(self.driver.find_element(*PageSameLink.get_answer_3).text))

        pass
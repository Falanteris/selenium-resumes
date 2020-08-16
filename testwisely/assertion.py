from selenium.webdriver.common.by import By

from testwisely.Switcher import Switcher


class AssertionTests(Switcher):
    link_locator = (By.PARTIAL_LINK_TEXT,"Assertion")
    get_text_content = (By.ID,"text")
    get_bold = (By.TAG_NAME,"b")
    get_italic = (By.TAG_NAME, "i")
    get_formatted = (By.ID,"formatted")
    def __init__(self,driver,logger):
        Switcher.__init__(self,driver,logger)

    def run(self):
        self.switch(AssertionTests.link_locator,self.operations)
        pass
    def operations(self,*args):
        text_content = self.driver.find_element(*AssertionTests.get_text_content)
        try:
            formatted = self.driver.find_element(*AssertionTests.get_formatted).text
            italic = text_content.find_element(*AssertionTests.get_italic).text
            bold = text_content.find_element(*AssertionTests.get_bold).text
            self.logger.debug(formatted)
            self.logger.debug(italic)
            self.logger.debug(bold)
            assert italic == "Italic"
            assert bold == "BOLD"
            assert "\n" in formatted
        except Exception as e:
            self.logger.error("Assertion is missing")

        pass

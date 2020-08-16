import time

from testwisely.Netbank import NetBank
from testwisely.helloworld import HelloWorld
from testwisely.survey import SurveyHandler
from testwisely.iframes import HandleIframes
from testwisely.pagesamelink import PageSameLink
from testwisely.popup import PopupWindow
from testwisely.assertion import AssertionTests
from testwisely.TableTest import TableHandle
class TestRunner():
    def test_hello_world(self,cross_browser):

        driver = cross_browser[0]

        optionals = cross_browser[2]

        logger = self.logger

        driver.get("https://testwisely.com/demo/")

        hello = HelloWorld(driver, logger)

        hello.run()
    def test_netbank(self,cross_browser):

        driver = cross_browser[0]

        optional = cross_browser[2]

        logger = self.logger

        netbank = NetBank(driver, logger)

        netbank.run(optional["account"],optional["value"])

    def test_survey(self,cross_browser):

        driver = cross_browser[0]

        optionals = cross_browser[2]

        logger = self.logger

        survey = SurveyHandler(driver,logger)

        survey.run(optionals["occupation"],
                   optionals["percentage"],
                   optionals["build"],
                   optionals["complaints"],
                   optionals["comments"])

    def test_iframe(self,cross_browser):
        driver = cross_browser[0]

        optionals = cross_browser[2]

        logger = self.logger

        iframe = HandleIframes(driver,logger)

        iframe.run()
    def test_same_link(self,cross_browser):

        driver = cross_browser[0]

        optionals = cross_browser[2]

        logger = self.logger

        same_link = PageSameLink(driver,logger)

        same_link.run()

    def test_pop_up(self,cross_browser):
        driver = cross_browser[0]

        optionals = cross_browser[2]

        logger = self.logger

        popup = PopupWindow(driver,logger)

        popup.run(optionals["alert"])

    def test_assertion(self,cross_browser):

        driver = cross_browser[0]

        optionals = cross_browser[2]

        logger = self.logger

        assertion = AssertionTests(driver,logger)

        assertion.run()

    def test_table(self,cross_browser):
        driver = cross_browser[0]

        optionals = cross_browser[2]

        logger = self.logger

        table = TableHandle(driver,logger)

        table.run(optionals["table"])



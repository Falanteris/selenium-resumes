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

        logger = self.logger

        driver.get("https://testwisely.com/demo/")

        hello = HelloWorld(driver, logger)

        hello.run()

        netbank = NetBank(driver, logger)

        netbank.run("Savings","50000")

        survey = SurveyHandler(driver,logger)

        survey.run("Developer","50%","weekly",["hard_to_write","manager_support"],"Cool stuff")

        iframe = HandleIframes(driver,logger)

        iframe.run()

        same_link = PageSameLink(driver,logger)

        same_link.run()

        popup = PopupWindow(driver,logger)

        popup.run("accept")

        assertion = AssertionTests(driver,logger)

        assertion.run()

        table = TableHandle(driver,logger)

        table.run("2898")



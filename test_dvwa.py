import time

from dvwautomation.login import LoginDvwa
from dvwautomation.sqlinject import SqlInject
class TestDvwa():

    def test_login_dvwa(self,cross_browser):
        # only works when DVWA has been fully configured
        # run this first always, to get the cookies for future usage.
        driver = cross_browser[0]
        logger = self.logger
        driver.get("http://172.17.0.2/")
        login = LoginDvwa(driver,logger)
        # login.use_cookie_login()
        # use change_difficulty method to change DVWA's difficulty.
        # login.login("admin","password")
        # login.change_difficulty("low")
        # time.sleep(1)
        # login.change_difficulty("medium")
        # time.sleep(1)
        # login.change_difficulty("high")
        # time.sleep(1)
        # login.change_difficulty("impossible")
        # time.sleep(1)
        # login.change_difficulty("low")
        # time.sleep(5)

    def test_sqli_dvwa(self,cross_browser):
        driver = cross_browser[0]
        logger = self.logger
        # commented lines are usable if you wish to do single testing
        # driver.get("http://172.17.0.2/")
        injector = SqlInject(driver,logger)
        # injector.use_cookie_login()
        injector.exploit()
        time.sleep(5)
        pass

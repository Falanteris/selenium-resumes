import time

from dvwautomation.login import LoginDvwa
from dvwautomation.sqlinject import SqlInject
from dvwautomation.xssinject import XssInjectReflected


class TestDvwa():

    def test_login_dvwa(self,cross_browser, dvwa_config_load):
        # only works when DVWA has been fully configured
        # run this first always, to get the cookies for future usage.
        driver = cross_browser[0]
        logger = self.logger
        credent = dvwa_config_load
        driver.get(credent["url"])
        login = LoginDvwa(driver,logger, credent["host"], credent["path"])
        login.login(credent["username"],credent["password"])

        # login.use_cookie_login()
        # use change_difficulty method to change DVWA's difficulty.
        # login.login("admin","password")
        login.change_difficulty_gui("Low")
        login.change_difficulty_gui("Medium")
        # time.sleep(1)
        login.change_difficulty_gui("High")
        # time.sleep(1)
        login.change_difficulty_gui("Impossible")
        # time.sleep(1)
        login.change_difficulty_gui("Low")
        time.sleep(5)

    def test_sqli_dvwa(self,cross_browser,dvwa_config_load):
        driver = cross_browser[0]
        logger = self.logger
        # commented lines are usable if you wish to do single testing
        # driver.get(dvwa_config_load["url"])
        injector = SqlInject(driver,logger, dvwa_config_load["host"],dvwa_config_load["path"])
        # injector.use_cookie_login()
        injector.exploit()
        time.sleep(5)
        pass
    def test_xss_dvwa(self,cross_browser,dvwa_config_load):
        driver = cross_browser[0]
        logger = self.logger
        # commented lines are usable if you wish to do single testing
        # driver.get(dvwa_config_load["url"])
        injector = XssInjectReflected(driver, logger, dvwa_config_load["host"], dvwa_config_load["path"])
        # injector.use_cookie_login()
        injector.exploit()
        time.sleep(5)
        pass
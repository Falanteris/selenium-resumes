import pytest


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("cross_browser")
class BaseClass:
    def select(self, WebElement,target):
        select = Select(WebElement)
        for opt in select.options:
            if opt.text  == target:
                opt.click()
                return True
        return AssertionError("Expected value missing..")
    def wait_for_presence(self, element, timer):
        waiter = WebDriverWait(self.driver,timer)
        return waiter.until(EC.presence_of_element_located(element))

    pass
@pytest.mark.usefixtures("wa_tester")
class WaClass:
    def select(self, WebElement,target):
        select = Select(WebElement)
        for opt in select.options:
            if opt.text  == target:
                opt.click()
                return True
        return AssertionError("Expected value missing..")
    pass

@pytest.mark.usefixtures("file_fixtures")
class FileTests:
    def select(self, WebElement,target):
        select = Select(WebElement)
        for opt in select.options:
            if opt.text  == target:
                opt.click()
                return True
        return AssertionError("Expected value missing..")
    pass
@pytest.mark.usefixtures("file_kbca")
class FileKbca:
    def select(self, WebElement,target):
        select = Select(WebElement)
        for opt in select.options:
            if opt.text  == target:
                opt.click()
                return True
        return AssertionError("Expected value missing..")
    pass

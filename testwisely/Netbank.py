from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from testwisely.Switcher import Switcher

WebDriverWait

class NetBank(Switcher):
    button = (By.ID, "transfer_btn")
    select_item = (By.NAME, "account")
    input_amount = (By.NAME, "amount")
    receipt = (By.ID, "receipt")
    receiptNo = (By.ID, "receiptNo")
    receiptDate = (By.ID, "date")
    partial_link = (By.LINK_TEXT,"NetBank")
    def __init__(self,driver,logger):
        Switcher.__init__(self,driver,logger)
    def run(self,acc_type,amt):
        self.switch(NetBank.partial_link,self.netbank_operation,acc_type,amt)
    def netbank_operation(self,*args):
        options = Select(self.driver.find_element(*NetBank.select_item)).options
        for option in options:
            if args[0] in option.text:
                self.logger.info("{} chosen".format(option.text))
                option.click()
                break
            self.logger.debug("{} Non-option".format(option.text))
        self.driver.find_element(*NetBank.input_amount).send_keys(args[1])
        self.driver.find_element(*NetBank.button).click()

        waiter = WebDriverWait(self.driver, 11)
        waiter.until(EC.text_to_be_present_in_element(NetBank.receipt, "Receipt No"))
        receipt = self.driver.find_element(*NetBank.receipt)
        self.logger.info(receipt.text)
        self.logger.info(receipt.find_element(*NetBank.receiptNo).text)
        self.logger.info(receipt.find_element(*NetBank.receiptDate).text)
import pickle

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class DvwaCookie():
    security_link_text = (By.LINK_TEXT,"DVWA Security")
    security_modifier = (By.NAME,"security")
    security_sender = (By.NAME,"seclev_submit")
    home_button = (By.LINK_TEXT,"Home")
    security_message = '//div[@class="message" and contains(text(),"{}")]'
    def __init__(self,storage,driver,logger,website, basepath):
        self.storage = storage
        self.driver = driver
        self.logger = logger
        self.index_website = website
        self.basepath = basepath
    def use_cookie_login(self):

        cookie_storage = pickle.load(open(self.storage,"rb"))

        for items in cookie_storage:
            self.driver.add_cookie(items)
        #self.driver.execute_script("location.reload()")
        self.driver.get(self.index_website)
    def save_cookie(self):
        pickle.dump(self.driver.get_cookies(),open(self.storage,"wb"))

    def change_difficulty(self,diff):
        security = self.driver.get_cookie("security")
        print(self.driver.get_cookies())
        security["value"] = diff
        print(security)

        self.driver.delete_cookie("security")
        self.driver.get("http://{}/{}".format(self.index_website,self.basepath))
        self.driver.add_cookie(security)

    def change_difficulty_gui(self,diff):
        self.driver.find_element(*DvwaCookie.security_link_text).click()
        select = Select(self.driver.find_element(*DvwaCookie.security_modifier))
        for opt in select.options:
            if opt.text == diff:
                opt.click()
        self.driver.find_element(*DvwaCookie.security_sender).click()

        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,DvwaCookie.security_message.format(diff.lower()))))
        except Exception as e:
            self.logger.error("Security message not found ..")
            raise e
        self.driver.find_element(*DvwaCookie.home_button).click()



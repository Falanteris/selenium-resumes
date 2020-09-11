from selenium.webdriver import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from dvwa_exploits.sqli_exploit import exploit
from dvwautomation.DvwaCookieManager import DvwaCookie


class SqlInject(DvwaCookie):
    linker = (By.XPATH,'//a[contains(text(),"SQL") and not(contains(text(),"Blind")) and contains(@href,"vulnerabilities")]')
    input_bar = (By.NAME,"id")
    button = (By.NAME,"Submit")
    responses = (By.CSS_SELECTOR,"div[class='vulnerable_code_area'] pre")
    def log_response(self,payload):
        self.logger.info("Payload Was : {}".format(payload))
        resps = self.driver.find_elements(*SqlInject.responses)
        for response in resps:
            self.logger.info("Got response : {}".format((response.text)))

        pass
    def __init__(self,driver,logger,host, basepath):
        DvwaCookie.__init__(self,'login.pkl',driver,logger,host, basepath)
    def exploit(self):
        self.driver.find_element(*SqlInject.linker).click()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(SqlInject.input_bar))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(SqlInject.button))

        exploit(self.fetch,self.log_response)

    def fetch(self):
        inp = self.driver.find_element(*SqlInject.input_bar)
        send = self.driver.find_element(*SqlInject.button)
        return {"input":inp,"button":send}


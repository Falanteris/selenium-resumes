from selenium.webdriver.common.by import By
from dvwa_exploits.xss_exploits import exploit
from dvwautomation.DvwaCookieManager import DvwaCookie
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class XssInjectReflected(DvwaCookie):
    linker = (By.XPATH,'//a[contains(text(),"XSS") and (contains(text(),"Reflected"))]')
    input_bar = (By.NAME,"name")
    button = (By.CSS_SELECTOR,"input[value='Submit']")
    responses = (By.CSS_SELECTOR,"div[class='vulnerable_code_area'] pre")
    def log_response(self,payload):
        self.logger.info("Payload Was : {}".format(payload))

        try:
            alert = self.driver.switch_to.alert
            self.logger.info("Got alert : {}".format((alert.text)))
            alert.accept()
        except Exception as e:
            self.logger.info("No alert")
        resps = self.driver.find_elements(*XssInjectReflected.responses)
        for response in resps:
            self.logger.info("Got response : {}".format((response.text)))

        pass
    def __init__(self,driver,logger,host, basepath):
        DvwaCookie.__init__(self,'login.pkl',driver,logger,host, basepath)
    def exploit(self):
        self.driver.find_element(*XssInjectReflected.linker).click()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(XssInjectReflected.input_bar))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(XssInjectReflected.button))

        exploit(self.fetch,self.log_response)

    def fetch(self):
        inp = self.driver.find_element(*XssInjectReflected.input_bar)
        send = self.driver.find_element(*XssInjectReflected.button)
        return {"input":inp,"button":send}


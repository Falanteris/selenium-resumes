

class Switcher():
    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger

    def switch(self,link_locator,func,*args):
        href = self.driver.find_element(*link_locator).get_attribute("href")
        self.driver.execute_script("window.open(arguments[0])",href)
        default = self.driver.window_handles[0]
        current = self.driver.window_handles[1]
        self.driver.switch_to.window(current)
        func(*args)
        self.driver.close()
        self.driver.switch_to.window(default)
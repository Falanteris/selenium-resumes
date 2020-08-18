import pickle
class DvwaCookie():
    index_website = "http://172.17.0.2/"
    def __init__(self,storage,driver,logger):
        self.storage = storage
        self.driver = driver
        self.logger = logger
    def use_cookie_login(self):

        cookie_storage = pickle.load(open(self.storage,"rb"))

        for items in cookie_storage:
            self.driver.add_cookie(items)
        #self.driver.execute_script("location.reload()")
        self.driver.get(DvwaCookie.index_website)
    def save_cookie(self):
        pickle.dump(self.driver.get_cookies(),open(self.storage,"wb"))

    def change_difficulty(self,diff):
        security = self.driver.get_cookie("security")
        security["value"] = diff
        self.driver.add_cookie(security)
        self.driver.execute_script("location.reload()")

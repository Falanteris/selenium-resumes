from selenium.webdriver import ActionChains as AC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tablify.dict import DictToTable
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import pytest
import time

from utilities.LogFormatClass import LogFormatClass


class TestRefreshers(LogFormatClass):
    title = (By.XPATH,"//h1[text()='Practice Page']")
    website = "https://rahulshettyacademy.com/AutomationPractice/"
    openWindow = (By.CSS_SELECTOR, "button[id='openwindow']")
    radioButtonList = (By.XPATH, "//div[@id='radio-btn-example']/fieldset/label/input[@type='radio']")
    autoCompleteBar = (By.ID, "autocomplete")
    search_bar_results = "//ul[@id='ui-id-1']/li[@class='ui-menu-item']/div[text()='{}']"
    select_dropdown = (By.ID, "dropdown-class-example")
    opentab_locator = (By.ID, "opentab")
    alert_components = {
        "name": (By.ID, "name"),
        "alert button": (By.ID, "alertbtn"),
        "confirm button": (By.ID, "confirmbtn")
    }

    checkboxes = (By.CSS_SELECTOR,
                  "div[class*='right-align'][id='checkbox-example'] fieldset label input[type='checkbox']"
                )
    hover_test = (By.ID,"mousehover")
    hide_textbox = (By.ID,"hide-textbox")
    show_textbox = (By.ID, "show-textbox")
    hover_test_home = (By.XPATH,"//a[text()='Top']")
    hover_test_reload = (By.XPATH, "//a[text()='Top']")
    table_value_locator = "//td[contains(text(),'{}')]/parent::tr/td"
    by_name_input = (By.NAME,"show-hide")
    iframe = (By.ID,"courses-iframe")
    courses_block = (
        By.CSS_SELECTOR,"[class*='courses-block'] [class='lower-content'] [class='upper-box'] h2 a"
    )
    def test_action_chains(self,cross_browser):

        driver = cross_browser[0]
        driver.get(TestRefreshers.website)
        actions = AC(driver)
        name_pair = TestRefreshers.hover_test
        driver.execute_script("window.scroll(0,1200)")
        actions.move_to_element(driver.find_element(*name_pair))
        actions.move_to_element(driver.find_element(*TestRefreshers.hover_test_home))
        actions.click()
        driver.execute_script("window.scroll(0,1200)")
        actions.move_to_element(driver.find_element(*name_pair))
        actions.move_to_element(driver.find_element(*TestRefreshers.hover_test_reload))
        actions.click()
        actions.perform()
        self.logger.info("Accomplished.. ActionChains rehearsal")
    def test_radio_buttons(self,cross_browser):

        driver = cross_browser[0]
        # driver.get(TestRefreshers.website)
        radios = driver.find_elements(*TestRefreshers.radioButtonList)
        for r in radios:
            r.click()
        self.logger.info("Accomplished.. RadioButtons rehearsal")
    def test_search_bar(self,cross_browser):

        driver = cross_browser[0]
        # driver.get(TestRefreshers.website)
        inp = driver.find_element(*TestRefreshers.autoCompleteBar)
        inp.send_keys("Afg")
        wait = WebDriverWait(driver,10)
        self.logger.info(TestRefreshers.search_bar_results.format("Afghanistan"))
        element = wait.until(EC.presence_of_element_located(
            (By.XPATH, TestRefreshers.search_bar_results.format("Afghanistan"))))
        element.click()
        self.logger.info("Accomplished.. Search Bar and WebDriverWait rehearsal")
    def test_select_dropdown(self,cross_browser):

        driver = cross_browser[0]
        # driver.get(TestRefreshers.website)
        select = driver.find_element(*TestRefreshers.select_dropdown)
        dropdown = Select(select)
        for options in dropdown.options:
            if options.text == "Option1":
                options.click()
        self.logger.info("Accomplished.. dropdown rehearsal")
    def test_check_box(self,cross_browser):

        driver = cross_browser[0]
        # driver.get(TestRefreshers.website)
        checkboxes = driver.find_elements(*TestRefreshers.checkboxes)
        [checkbox.click() for checkbox in checkboxes]
        self.logger.info("Accomplished.. checkbox rehearsal")
    def test_window_switch(self,cross_browser):

        driver = cross_browser[0]
        # driver.get(TestRefreshers.website)
        driver.find_element(*TestRefreshers.openWindow).click()
        handles = driver.window_handles
        default_window = handles[0]
        new_window_1 = handles[1]
        driver.switch_to.window(new_window_1)
        driver.close()
        driver.switch_to.window(default_window)
        self.logger.info("Accomplished.. window switch rehearsal")

    def test_open_tab(self,cross_browser):

        driver = cross_browser[0]
        # driver.get(TestRefreshers.website)
        driver.find_element(*TestRefreshers.opentab_locator).click()
        handles = driver.window_handles
        default_window = handles[0]
        new_window = handles[1]
        driver.switch_to.window(new_window)
        self.logger.info(driver.title)
        driver.switch_to.window(default_window)
        driver.find_element(*TestRefreshers.opentab_locator).click()
        handles = driver.window_handles
        driver.switch_to.window(handles[2])
        self.logger.info(driver.title)
        driver.close()
        driver.switch_to.window(handles[1])
        driver.close()
        driver.switch_to.window(default_window)

    def test_alert_handles(self,cross_browser):

        driver = cross_browser[0]
        alertbtn = TestRefreshers.alert_components["alert button"]
        inputbar = TestRefreshers.alert_components["name"]
        confirm = TestRefreshers.alert_components["confirm button"]
        name = "Cinder"
        # driver.get(TestRefreshers.website)
        driver.find_element(*inputbar).send_keys(name)
        driver.find_element(*alertbtn).click()
        alert = driver.switch_to.alert
        assert name in alert.text
        self.logger.info("alert contains your name")
        alert.accept()
        driver.find_element(*inputbar).send_keys(name)
        driver.find_element(*confirm).click()
        alert = driver.switch_to.alert
        assert name in alert.text
        self.logger.info("confirm pop-up contains your name")
        alert.accept()

    def test_table_handling(self, cross_browser):

        driver = cross_browser[0]
        # driver.get(TestRefreshers.website)
        table_values = driver.find_elements(By.XPATH, TestRefreshers.table_value_locator.format("25"))
        dataset = list()
        counter = 0
        headers = ["Instructor","Courses","Price"]
        subdata = dict()
        for data in table_values:
            subdata[headers[counter]] = data.text
            counter+=1
            if counter>2:
                counter = 0
                dataset.append(subdata)
                subdata = dict()
            self.logger.info(subdata)
            dataset.append(subdata)
        table = DictToTable()
        table.add_data(headers,True)
        for subdata in dataset:
            temp = list()
            for val in subdata.values():
                temp.append(val)
            table.add_data(temp,False)
        with open("report/table_example.html","w") as f:
            f.write(table.commit())
        pass
    def test_hide_show(self,cross_browser):

        driver = cross_browser[0]
        # driver.get(TestRefreshers.website)
        driver.find_element(*TestRefreshers.by_name_input).send_keys("kekmock")
        driver.find_element(*TestRefreshers.hide_textbox).click()
        try:
            driver.find_element(*TestRefreshers.by_name_input)
            assert "hidden" == False
        except Exception as e:
            pass
        driver.find_element(*TestRefreshers.show_textbox).click()
        driver.find_element(*TestRefreshers.by_name_input).clear()
        driver.find_element(*TestRefreshers.by_name_input).send_keys("test")

    def test_iframe(self,cross_browser):

        driver = cross_browser[0]
        # driver.get(TestRefreshers.website)
        driver.switch_to.frame(driver.find_element(*TestRefreshers.iframe))
        courses = driver.find_elements(*TestRefreshers.courses_block)
        for course in courses:
            self.logger.info(course.text)
        driver.switch_to.default_content()
        self.logger.info(driver.find_element(*TestRefreshers.title).text)








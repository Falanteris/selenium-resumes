import json

import pytest
from selenium import webdriver
from utilities.LogFormatClass import LogFormatClass
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import random
driver = None



CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver' # replace this with your Chrome driver location
FIREFOXDRIVER_PATH = '/home/jasperzec/geckodriver' # replace this with your Firefox driver location

def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="The name of the browser, defaults to both if not included"
    )
    parser.addoption(
        "--testtype", default="flight", help="Type of trip you wish to test"
    )


@pytest.fixture(scope='module')
def config_firefox():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--start-maximized")
    return firefox_options


@pytest.fixture(scope='module')
def config_firefox_headless():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--start-maximized")
    firefox_options.add_argument("headless")
    return firefox_options


@pytest.fixture(scope='module')
def config_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("headless")
    return chrome_options


@pytest.fixture(scope='module')
def config_chrome_headless():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("headless")
    return chrome_options



@pytest.fixture(scope='class',params=[json.loads(open("file_params/test_dvwa_auth.json").read())])
def dvwa_config_load(request):
    yield request.param

@pytest.fixture(scope='class')
def cross_browser(request, config_chrome, config_firefox):
    # index 0 is the PATH to the driver
    # index 1 is the webdriver instantiator
    # index 2 is the browser type
    driver_inst_chrome = webdriver.Chrome
    driver_inst_firefox = webdriver.Firefox

    pref_browser = request.config.getoption("--browser")
    optionals = json.loads(open("file_params/test_wisely.json").read())
    logger = LogFormatClass()
    request.cls.logger = logger.get_logger_format_default()
    set_up = []
    driver_inst = None
    # request.cls.params = [driver_inst(executable_path=driver_addr, options=config_firefox), random_wa_message(pref_browser)]
    if pref_browser == "firefox":
        driver_inst = driver_inst_firefox(GeckoDriverManager().install(),options=config_firefox)
        # agent = driver_inst.execute_script("return navigator.userAgent")

        set_up = [driver_inst, pref_browser,
                optionals]
    else:
        driver_inst = driver_inst_chrome(ChromeDriverManager().install(),options=config_chrome)
        # agent = driver_inst.execute_script("return navigator.userAgent")

        set_up = [driver_inst, pref_browser, optionals]
    yield set_up
    driver_inst.close()

# print("Executing tests on both browsers")
# yield [driver_inst_firefox(executable_path=FIREFOXDRIVER_PATH, options=config_firefox), "firefox"]
# return [driver_inst_chrome(executable_path=CHROMEDRIVER_PATH, options=config_chrome), "chrome"]

@pytest.fixture(
    params=[(CHROMEDRIVER_PATH, webdriver.Chrome, "chrome"), (FIREFOXDRIVER_PATH, webdriver.Firefox, "firefox")])
def cross_browser_headless(request, config_chrome_headless, config_firefox_headless):
    driver_addr = request.param[0]
    driver_inst = request.param[1]
    if request.param[2] == "firefox":
        request.cls.driver = driver_inst(executable_path=driver_addr, options=config_firefox_headless)
    else:
        request.cls.driver = driver_inst(executable_path=driver_addr, options=config_chrome_headless)
    request.cls.browser = request.param[2]
    yield
    request.cls.driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url('http://www.example.com/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Failed XD</div>'))
        report.extra = extra
    report.extra = extra
# @pytest.fixture(scope='module')
# def random_wa_message():
# 	# generates a random WA message based on the browser.
# 	def initiate(browser):
# 		wa_message_shuffle = ["Ok Pa", "Ok", "Sip"]
# 		wa_message_ender = "-- this message was sent using {} browser".format(browser)
# 		message = wa_message_shuffle[random.randint(0,len(wa_message_shuffle)-1)]
# 		return message+wa_message_ender
# 	return initiate
# @pytest.fixture(params=[(CHROMEDRIVER_PATH,webdriver.Chrome,"chrome"),(FIREFOXDRIVER_PATH,webdriver.Firefox,"firefox")])
# def wa_tester(request,config_chrome,config_firefox,random_wa_message):
# 	# index 0 is the PATH to the driver
# 	# index 1 is the webdriver instantiator
# 	# index 2 is the browser type
# 	driver_addr = request.param[0]
# 	driver_inst = request.param[1]
# 	if request.param[2] == "firefox":
# 		return [driver_inst(executable_path=driver_addr, options=config_firefox), random_wa_message(request.param[2])]
#
# 	return [driver_inst(executable_path=driver_addr,options=config_chrome),random_wa_message(request.param[2])]

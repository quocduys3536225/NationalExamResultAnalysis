import inspect
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = None

class BaseClass:
    def __init__(self):
        option = webdriver.ChromeOptions()
        # Working with the 'add_argument' Method to modify Driver Default Notification
        option.add_argument('--disable-notifications')
        option.add_argument('--headless')
        #option.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})

        driver = webdriver.Chrome(executable_path=(r"C:\Users\Admin\.wdm\drivers\chromedriver\win32\103.0.5060.53\chromedriver.exe"), chrome_options= option)
        #driver.set_page_load_timeout(1)
        driver.maximize_window()
        self.driver = driver
        #yield
        #self.driver.close()

    def getLogger(self):
        loggerName = inspect.stack()[1][3] # to get correct file name
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.WARNING)
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))


    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)


    def close_brower(self):
        self.driver.close()
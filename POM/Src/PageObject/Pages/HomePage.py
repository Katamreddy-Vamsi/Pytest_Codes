import os
import sys

# from Src.PageObject.Locators import Locator
from POM.Src.PageObject.Locators import Locator
from selenium.webdriver.common.by import By

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))  # import os
# Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())


class Home(object):
    def __init__(self, driver):
        self.driver = driver
        self.logo = driver.find_element(By.XPATH, Locator.logo)
        self.search_text = driver.find_element(By.XPATH, Locator.search_text)
        self.submit = driver.find_element(By.XPATH, Locator.submit)

    def getSearchText(self):
        return self.search_text

    def getSubmit(self):
        return self.submit

    def getWebPageLogo(self):
        return self.logo

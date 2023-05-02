from selenium.webdriver.common.by import By


class GoogleSearch:
    search_text = (By.XPATH, "//textarea[@name='q']")
    submit_button = (By.XPATH, "(//input[@name='btnK' and @role='button'])[2]")
    logo = (By.XPATH, "//img[@class='lnXdpd']")

    def __init__(self, driver):
        self.driver = driver

    def getSearchText(self):
        return self.driver.find_element(*GoogleSearch.search_text)

    def getSubmit(self):
        return self.driver.find_element(*GoogleSearch.submit_button)

    def getWebPageLogo(self):
        return self.driver.find_element(*GoogleSearch.logo)
 # edited

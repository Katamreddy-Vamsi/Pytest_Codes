from selenium.webdriver.common.by import By

from Src.Pages.GenericMethodsPage import GenericMethodsPage
from Src.Pages.GoogleSearchResultPage import GoogleSearchResultPage


class GoogleSearchEnginePage(GenericMethodsPage):

    SEARCH_FIELD = (By.XPATH, "//textarea[@title = 'Search']")
    SEARCH_BUTTON = (By.XPATH, "//div[@class = 'FPdoLc lJ9FBc']//input[@value = 'Google Search']")

    def __init__(self, driver):
        super().__init__(driver)

        self.driver.get("https://www.google.com/")
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

    def enter_text_to_search_engine(self):
        self.send_text_to_element(self.SEARCH_FIELD, "LambdaTest")

    def click_on_search_button(self):
        self.click_on_element(self.SEARCH_BUTTON)

    def get_google_search_engine_title(self, title):
        return self.get_title(title)

    def do_all_actions_in_search_engine_page(self):
        self.send_text_to_element(self.SEARCH_FIELD, "LambdaTest")
        self.click_on_element(self.SEARCH_BUTTON)
        return GoogleSearchResultPage(self.driver)




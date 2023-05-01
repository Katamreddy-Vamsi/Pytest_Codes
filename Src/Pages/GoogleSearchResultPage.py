from selenium.webdriver.common.by import By

from Src.Pages.GenericMethodsPage import GenericMethodsPage


class GoogleSearchResultPage(GenericMethodsPage):

    LAMBD_TEST_LINK = (By.XPATH, "//h3[@class = 'LC20lb MBeuO DKV0Md' and text() ='LambdaTest: Most Powerful Cross Browser Testing Tool Online']")


    def __init__(self, driver):
        super().__init__(driver)

    def result_page_title(self, title):
        return self.get_title(title)

    def visibility_of_specific_link_text(self):
        if self.is_visible(self.LAMBD_TEST_LINK):
            return self.get_element_text(self.LAMBD_TEST_LINK)

    def click_on_lambda_test_link(self):
        self.click_on_element(self.LAMBD_TEST_LINK)










import time

from selenium.webdriver import Keys

import sys

sys.path.insert(0, "..")
from Google_Search.utilities.base_class import Base_Test
from Google_Search.pages.GoogleSearchPage import GoogleSearch


class TestCase_01(base_class):
    def test_testcase_01(self):
        google_search = GoogleSearch(self.driver)
        web_page_title = "Google"
        try:
            if self.driver.title == web_page_title:
                print("WebPage loaded successfully")
                self.assertEqual(self.driver.title, web_page_title)
        except Exception as error:
            print(error)
        google_search.getSearchText().send_keys("Lamda Test")
        time.sleep(2)
        google_search.getSearchText().send_keys(Keys.ENTER)
        # google_search.getSubmit().click()
        time.sleep(2)
        print(self.driver.title)
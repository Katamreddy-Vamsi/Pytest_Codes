import time

from Src.Pages.GoogleSearchEnginePage import GoogleSearchEnginePage
from Tests.test_base import BaseTest


class TestGoogleSearch(BaseTest):

    def test_google_search_title_assertion(self):
        self.google_search_engine_page = GoogleSearchEnginePage(self.driver)
        title = self.google_search_engine_page.get_title('Google')
        assert title == 'Google'

    def test_click_on_search_and_check_title_assertion(self):
        self.google_search_engine_page = GoogleSearchEnginePage(self.driver)
        self.google_search_engine_page.enter_text_to_search_engine()
        self.google_search_engine_page.click_on_search_button()


        


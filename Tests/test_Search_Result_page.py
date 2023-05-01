import time

from Src.Pages.GoogleSearchEnginePage import GoogleSearchEnginePage
from Src.Pages.GoogleSearchResultPage import GoogleSearchResultPage
from Tests.test_Search_Engine_page import TestGoogleSearch
from Tests.test_base import BaseTest


class TestSearchResult(BaseTest):

    def test_result_page_title(self):
        self.google_search_engine_page = GoogleSearchEnginePage(self.driver)
        google_search_result_page = self.google_search_engine_page.do_all_actions_in_search_engine_page()
        title = google_search_result_page.get_title('LambdaTest - Google Search')
        assert title == 'LambdaTest - Google Search'

    def test_visibility_of_specific_link(self):
        self.google_search_engine_page = GoogleSearchEnginePage(self.driver)
        google_search_result_page = self.google_search_engine_page.do_all_actions_in_search_engine_page()
        text_value = google_search_result_page.visibility_of_specific_link_text()
        assert text_value == 'LambdaTest: Most Powerful Cross Browser Testing Tool Online'


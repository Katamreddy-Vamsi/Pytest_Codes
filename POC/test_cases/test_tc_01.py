import time

from selenium.webdriver import Keys

import sys

sys.path.insert(0, "..")

from POC.Config.base_class import base_class
from POC.Pages.Home_Page import Air


# TestCases_01 is class & it contains all test cases. .
class TestCase_01(base_class):

    def test_testcase_01(self):
        Air_india = Air(self.driver)
        web_page_title = "Air India"
        try:
            if self.driver.title == web_page_title:
                print("WebPage loaded successfully")
                self.assertEqual(self.driver.title, web_page_title)
        except Exception as error:
            print(error)

        # click on logo
        Air_india.logos().click()
        self.driver.implicitly_wait(10)
        # click on one way
        Air_india.one_way_click()
        self.driver.implicitly_wait(10)
        # send BKK for starting destination.
        Air_india.From_place().send_keys("BKK")
        self.driver.implicitly_wait(10)
        # click on  BKK for starting destination.
        Air_india.From_place_click().click()
        self.driver.implicitly_wait(10)
        # send delhi for ending destination.
        Air_india.To_place().send_keys("Delhi")
        self.driver.implicitly_wait(10)
        # click on last  destination.
        Air_india.To_place_click().click()
        self.driver.implicitly_wait(10)
        # click on date calender.
        Air_india.date_calender().click()
        self.driver.implicitly_wait(10)
        # select the date from calendar.
        Air_india.date_calender_click().click()
        self.driver.implicitly_wait(10)
        # select the passenger
        Air_india.passenger_box().click()
        self.driver.implicitly_wait(10)
        # add the Passenger
        Air_india.Passenger_plus().click()
        self.driver.implicitly_wait(10)
        # check the class of flight.
        Air_india.flight_classwise().click()
        self.driver.implicitly_wait(10)
        # select the flight class.
        Air_india.flight_class_select().click()
        self.driver.implicitly_wait(10)
        # select the show flight.
        Air_india.Show_Flight_click().click()
        self.driver.implicitly_wait(10)

        print(self.driver.title)

from selenium.webdriver.common.by import By


# All Locators.
class Air:
    one_way = (By.XPATH, "//input[@id='mat-radio-2-input']")
    logo = (By.XPATH, "//img[@title = 'Air India Logo']")
    Accept_all = (By.XPATH, "//div[@id='c-bns']/button[text()'Accept all']")
    From = (By.XPATH, "//input[@id='From']")
    From_Click = (By.XPATH, "//span[text()='BKK']")
    To = (By.XPATH, "//input[@id='To']")
    To_click = (By.XPATH, "//div[text()=' Delhi, India, IN ']")
    Show_Flight = (By.XPATH, "//button[text()=' SHOW FLIGHTS ']")
    date_Select = (By.XPATH, "//*[@id='mat-tab-content-0-0']/div/app-search-flight/div/form/div["
                             "1]/app-datepicker-range-popup/div/div[1]/div[2]/input[2]")
    date_click = (By.XPATH, "//*[@id='mat-tab-content-0-0']/div/app-search-flight/div/form/div["
                            "1]/app-datepicker-range-popup/div/div[1]/div[1]/div/ngb-datepicker/div[2]/div["
                            "2]/ngb-datepicker-month/div[6]/div[1]/span")
    passenger = (By.XPATH, "//*[@id='dropdownForm1']")
    passenger_add = (By.XPATH, "//*[@id='mat-tab-content-0-0']/div/app-search-flight/div/form/div["
                               "1]/app-add-passenger/div/div[2]/div[1]/div[2]/button[2]")
    flight_class = (By.XPATH, "//*[@id='mat-tab-content-0-0']/div/app-search-flight/div/form/div[1]/app-class-type")
    flight_P = (By.XPATH, "//*[@id='mat-option-2']/span")

    def __init__(self, driver):
        self.driver = driver

    def Accept_link(self):
        return self.driver.find_element(*Air.Accept_all)

    def one_way_click(self):
        button = self.driver.find_element(By.XPATH, "//input[@id='mat-radio-2-input']")

        return self.driver.execute_script("arguments[0].click();", button)

    def logos(self):
        return self.driver.find_element(*Air.logo)

    def From_place(self):
        return self.driver.find_element(*Air.From)

    def From_place_click(self):
        return self.driver.find_element(*Air.From_Click)

    def To_place(self):
        return self.driver.find_element(*Air.To)

    def To_place_click(self):
        return self.driver.find_element(*Air.To_click)

    def date_calender(self):
        return self.driver.find_element(*Air.date_Select)

    def date_calender_click(self):
        return self.driver.find_element(*Air.date_click)

    def passenger_box(self):
        return self.driver.find_element(*Air.passenger)

    def Passenger_plus(self):
        return self.driver.find_element(*Air.passenger_add)

    def flight_classwise(self):
        return self.driver.find_element(*Air.flight_class)

    def flight_class_select(self):
        return self.driver.find_element(*Air.flight_P)

    def Show_Flight_click(self):
        return self.driver.find_element(*Air.Show_Flight)

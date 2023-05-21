import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.airindia.com/")

# driver = webdriver.Chrome(executable_path= r"C:\Users\7000033861\Downloads\chromedriver_win32\chromedriver.exe")

driver.maximize_window()
driver.delete_all_cookies()
# driver.find_element(By.XPATH, "//img[@title = 'Air India Logo']").click()
time.sleep(10)
# driver.find_element(By.XPATH, "//*[@id='mat-tab-content-0-0']/div/app-search-flight/div/form/div[1]/app-datepicker-range-popup/div/div[1]/div[2]/input[2]").click()
# driver.find_element(By.XPATH, "//input[@id='From']").send_keys("delhi")
# time.sleep(10)
#
# time.sleep(15)
# button = driver.find_element(By.XPATH, "//input[@id='mat-radio-2-input']")
# driver.execute_script("arguments[0].click();", button )


# time.sleep(10)
# driver.find_element(By.XPATH,"//*[@id='mat-tab-content-0-0']/div/app-search-flight/div/form/div[1]/app-datepicker-range-popup/div/div[1]/div[1]/div/ngb-datepicker/div[2]/div[2]/ngb-datepicker-month/div[6]/div[1]").click()
# time.sleep(10)
driver.find_element(By.XPATH, "//*[@id='dropdownForm1']").click()
time.sleep(7)
driver.find_element(By.XPATH, "//*[@id='mat-tab-content-0-0']/div/app-search-flight/div/form/div[1]/app-add-passenger/div/div[2]/div[1]/div[2]/button[2]").click()
time.sleep(7)
driver.find_element(By.XPATH, "//*[@id='mat-tab-content-0-0']/div/app-search-flight/div/form/div[1]/app-class-type").click()
time.sleep(7)
driver.find_element(By.XPATH, "//*[@id='mat-option-2']/span").click()
time.sleep(7)


driver.quit()
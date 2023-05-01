import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com/")
driver.maximize_window()
driver.delete_all_cookies()
driver.find_element(By.XPATH, "//textarea[@title = 'Search']").send_keys("LambdaTest")
driver.find_element(By.XPATH, "//div[@class ='FPdoLc lJ9FBc']//input[@value = 'Google Search']").click()
time.sleep(10)
driver.find_element(By.PARTIAL_LINK_TEXT, "LambdaTest Automation").click()
time.sleep(10)
driver.quit()


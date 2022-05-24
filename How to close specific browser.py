from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

#1. Browser 1
driver.get("https://opensource-demo.orangehrmlive.com/")


#2. Browser 2
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowIDS=driver.window_handles

#parentid = windowIDS[0]
#childid = windowIDS[1]

#print(parentid,childid)

#3. Using for loop to open multiple browsers:
for wID in windowIDS:
    driver.switch_to.window(wID)
    print(driver.title)
    if driver.title=="OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS":

        driver.close()
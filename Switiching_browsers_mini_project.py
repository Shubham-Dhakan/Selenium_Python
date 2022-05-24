from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait

import time

driver = webdriver.Chrome()
driver.maximize_window()                # maximizes_window
mywait = WebDriverWait(driver,10)       # < explicit wait > declared globally

driver.get("http://testautomationpractice.blogspot.com/")
print(driver.title)
print(driver.current_url)
driver.implicitly_wait(10)              # < implicit wait > declared gloablly

#1 Handling Alert Pop-up
click_button = driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()

myalert = driver.switch_to.alert          #It will switch to alert
print(myalert.text)
myalert.accept()                          #It will close pop-up with < accept/ok > option

#2 Identifying SearchBox ELement:
searchbox = driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("selenium")
searchbutton = driver.find_element(By.CLASS_NAME,"wikipedia-search-button").click()

#3 Calling Multiple Webpages:
websites = driver.find_elements(By.XPATH,"//div[@id='Wikipedia1_wikipedia-search-results']//a")
print(len(websites))                #5 webpages

for website in websites:
    website.click()                 #It will open all targeted webpages

website = driver.window_handles     #window_handles is used to return id when we open more than 1 webpage
mainid = website[0]
secondid = website[1]
thirdid = website[2]
fourthid = website[3]
fifthid = website[4]

print(mainid,secondid,thirdid,fourthid,fifthid)

#4 Switching browsers:


for webpage in website:
    driver.switch_to.window(webpage)
    print(webpage.title)

driver.quit()        #Recommended   # Will close all browsers with chrome process
#driver.close()                     # Will close driver focused browser only and back end process will
                                    # remain active

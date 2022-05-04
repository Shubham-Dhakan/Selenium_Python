from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.ebay.ca/")
time.sleep(2)

# ALL Navigation Command
driver.get("https://www.amazon.ca/")
driver.maximize_window()
time.sleep(2)

driver.back()                               # "back" command will go back to ebay.ca
time.sleep(2)

#driver.forward()                            # "forward" command will take back to amazon.ca
#time.sleep(2)

#driver.refresh()                            # "refresh" command will refresh once
#driver.back()                               # "back" command will go back to ebay.ca

# ALL Application command
print(driver.title)                         # "title" is command
print(driver.current_url)                   # "current_url" is command
#print(driver.page_source)

# Locator Matching with single element
searchbox = driver.find_element(By.XPATH,"//input[@id='gh-ac']")
searchbox.send_keys("Apple Iphone 13 Pro")

# All conditional command
print("display status:",searchbox.is_displayed())           # "display" command will check selected element is displayed or not
print("enable status:",searchbox.is_enabled())              # "enable" command will check selected element is enabled or not
print("selected status:",searchbox.is_selected())           # "selected" command usually selects radio bttn or check box

#driver.close()                             #It will close driver focused browser "ebay.ca"
driver.quit()                               #It will close all browsers and kill back-end driver process 








 #TEST CASE:
#1. Finding window_handle of single browser
#2. Finding window_handles of mutliple_browsers

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

#1. Finding window_handle of single browser
driver.get("https://opensource-demo.orangehrmlive.com/")
#windowid = driver.current_window_handle       #current_window_handle --> < command > returns current window ID
                                               # Everytime the window id will be different

print(driver.title)                                       #title --> method
print(driver.current_url)                                 #current_url --> method
#print(parentwindowid)


#2. Finding window_handles of mutliple_browsers
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
print(driver.title)
print(driver.current_url)
windowids=driver.window_handles

parentwID = windowids[0]    # It returns driver focused window id always < [0] >
childwID = windowids[1]     # It returns following window id always

print(parentwID,childwID)   # 793100A167C1205AFDC782B9A1283256
                            # D2ACE763C2C4E39232022C991EA6DE67

driver.switch_to.window(childwID)
print("child window id title:",driver.title)

driver.switch_to.window(parentwID)
print("parent window id title:",driver.title)

#driver.close()              # It will close driver focused window
#driver.quit()              # It will close all browser window and chromedriver process.


        # NOTE: [" If you run this code for 5 times, it will return different window ID's 5 times,"]
                            # < This is how selenium Works >

                # We will never find window handles on webpage anywhere.
            # current_window_handle is dynamic as it changes everytime when called
                            # < This is how selenium Works >

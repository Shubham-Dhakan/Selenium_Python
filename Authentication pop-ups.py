from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
import time

driver = webdriver.Chrome()

#Method1: First Call without Injection concept:
#driver.get("https://the-internet.herokuapp.com/basic_auth")               # Normally we are calling webpage
                                                                           # No syntax used in this #URL

#Method2: Calling Injection Concept: < SOLUTION > for authentication-pop/ups
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")    # username:password@ " is < SYNTAX > of injection concept
                                                                           # " admin:admin@ " is < SYNTAX >
                                                                           # Always use it in Webpage #URL
                                                                           # It will < BYPASS > authentication pop-up
print(driver.title)                     # title --> method
print(driver.current_url)               # current_url --> method

time.sleep(2)
driver.quit()
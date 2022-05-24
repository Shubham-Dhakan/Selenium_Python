from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

opts = webdriver.ChromeOptions()                    #This will aid us to get access of Browser <Setting>
opts.add_argument("--disable notification")         #This will disable notification pop-up

driver = webdriver.Chrome()
driver.implicitly_wait(5)                           #Globaly declaring < impicit wait >
mywait = WebDriverWait(driver,10)                   #Globaly declaring < explicit wait >


driver.get("---- some website ---- ")
driver.maximize_window()

print(driver.title)                                 #title --> method
print(driver.current_url)                           #current_url --> method

driver.close()
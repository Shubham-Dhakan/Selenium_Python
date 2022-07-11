from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)           # Declaring Globally so it applies to element where required

driver.get("https://www.honda.ca")
#driver.switch_to.new_window('window')          # it will open 2 windows
driver.switch_to.new_window('Tab')              # it will open 2 tabs
driver.get("https://www.toyota.ca")

driver.close()

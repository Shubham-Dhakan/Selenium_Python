#TestCase:
#1. Open Web Browser (Chrome/Firefox/Internet Explorer)
#2. Open Url http://
#3. Identify elements through LinkTest locator
#4. Identify elements through PartialLink Test locator
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service

#1 Open Web Browser (Chrome/Firefox/Internet Explorer)
#ser_obj = Service("C:\\Program Files\\Python310\\Scripts\\chromedriver.exe")
driver = webdriver.Chrome()

#2 Open Url http://
driver.get("https://www.honda.ca/")
driver.maximize_window()
time.sleep(5)

#3. Identify elements through LinkTest locator
driver.find_element(By.LINK_TEXT,"Models").click()

#4. Identify elements through PartialLink Test locator
#driver.find_element(By.PARTIAL_LINK_TEXT,"Mod").click()



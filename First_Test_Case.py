#Test Case:
#1. Open Web Browser (Chrome/Firefox/Internet Explorer)
#2. Open Url http://
#3. Provide Email
#4. Provide Password
#5. Click on login
#6. Capture tittle of the dashboard page.
#7. Verify tittle of the page:
#8. Close browser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
import time

#1.Open Web Browser (Chrome/Firefox/Internet Explorer)
#serv_obj = Service("C:\\Users\\Hp\\PycharmProjects\\SeleniumPython\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome()
#driver = webdriver.Chrome("Service=serv_obj")

#2.Open Url http://
driver.get("https://www.amazon.ca/")
print(driver.title)
driver.find_element_by_xpath("//*[@id='nav-link-accountList']").click()

#3,4,5 Provide Email, Provide Password, Click on login
driver.find_element(By.ID,"ap_email").send_keys("------")                  # enter your Email_id in send_keys
driver.find_element(By.ID,"continue").click()
driver.find_element(By.NAME,"password").send_keys("-------")               # enter your Password in send_keys
driver.find_element(By.ID,"auth-signin-button").click()

#6.Capture tittle of the dashboard page.
act_title = driver.title
exp_title = "Amazon.ca: Low Prices – Fast Shipping – Millions of Items"

#7.Verify tittle of the page:
if act_title==exp_title:
    print("test is passed")
else:
    print("test is failed")

time.sleep(10)

#8.Quit
driver.quit()


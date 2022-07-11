from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
print(driver.title)
print(driver.current_url)
print(driver.current_window_handle)

#Scroll down to element method:
delivery_options = driver.find_element(By.XPATH,"//span[@id='select2-reasondummy-container']").click()
#driver.execute_script("arguments[0].scrollintoview;",delivery_options)
#value = driver.execute_script("window.pageYOffset;")
#print(value)

option_list= driver.find_elements(By.XPATH,"//*[@id='select2-reasondummy-results']/li")
print(len(option_list))

for options in option_list:
    if options.text=="Visa extension":
        options.click()
        break

driver.close()
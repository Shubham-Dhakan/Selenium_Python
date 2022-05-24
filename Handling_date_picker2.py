from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
print(driver.title)                             # title --> method
print(driver.current_url)                       # current_url --> method
print(driver.current_window_handle)             # returns webpage --> ID

date_of_birth = driver.find_element(By.XPATH,"//*[@id='dob']").click()

month = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
month.select_by_visible_text("Aug")
year = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
year.select_by_visible_text("1999")

#table = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr/td")
table = driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']//tbody/tr/td")
for date in table:
    if date.text=="26":
        date.click()
        break;




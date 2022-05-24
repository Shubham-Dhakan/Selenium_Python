from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://jqueryui.com/demos/")
print(driver.title)                             # title --> method
print(driver.current_url)                       # current_url --> method
print(driver.current_window_handle)             # returns webpage --> ID


datepicker = driver.find_element(By.LINK_TEXT,"Datepicker")
datepicker.click()

# DATE PICKER IS INSIDE FRAME ELEMENT:
driver.switch_to.frame(0)                       # Using index number concept:
                                                # We only have one frame so using '0'

# FORMAT --> mm/dd/yyyy                          # This is manual way of selecting a date.
#searchbox = driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("08/26/1999")


# Using < LOGIC > to find out date:
# FIRST WRITE DOWN OUR DESIRED DATE

month="August"
year="2023"
date="26"

searchbox = driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

# NOW we will use 'WHILE' Loop because we don't know the end point.
while True:                             # We are declaring this loop as true:
    m=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    y=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if m=="August" and y=="2022":
        break;
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

# Now we are selecting specific date from table:
date_from_table = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr/td")

for dates in date_from_table:
    if dates.text==date:
        dates.click()
        break;
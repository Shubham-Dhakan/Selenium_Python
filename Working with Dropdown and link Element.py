from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
import requests

driver = webdriver.Chrome()
driver.implicitly_wait(10)                      # implicit wait
mywait = WebDriverWait(driver,10)               # explicit wait


driver.get("https://www.ebay.ca/")
print(driver.title)                             # title --> method  (application command)
print(driver.current_url)                       # current_url --> method    (application command)

#1. Testing searchbox element
searchbox = driver.find_element(By.ID,"gh-ac")     # ID --> LOCATOR
searchbox.send_keys("iphone 13 pro max")
print(searchbox.get_attribute("value"))            # get_attribute  will print search value
print("display status:",searchbox.is_displayed())  # It will verify that element is displayed or not (conditional Command)
print("enable status:",searchbox.is_enabled())     # It will verify that element is selected or not  (conditional Command)
searchbox.submit()                                 # submit() will work as enter/button

driver.back()                                      # It will navigate to previous Page

#2. Testing Dropdown Element
category = Select(driver.find_element(By.XPATH,"//*[@id='gh-cat']"))
#category.click()                                  #click() function wont work with select()

        # Calling sub-element of category elements through select() - 3 built in method

#category.select_by_index("2")                       # built-in method (NOTE: ALL ARE CASE SENSITIVE)
#category.select_by_value("550")                     # buitl-in method  (NOTE: ALL ARE CASE SENSITIVE)
category.select_by_visible_text("Art")               # most prefered method (NOTE: ALL ARE CASE SENSITIVE)


#3. Testing all sub-elements in Category element by #TWO methods.
#Method-1
option = category.options               # "options" is --> method, so we dont have to use locators
print(len(option))                      # it will return total number of option element


#Mehtod-2
#option = driver.find_elements(By.TAG_NAME,"option")    # Using locator we are calling "option element"
#print(len(option))

#Mehtod-3 < USE THIS METHOD WHEN WE DONT HAVE "select" tag in dropdown Element.
#option = driver.find_elements(By.XPATH,"//*[@id='gh-cat']/option")    # Using XPATH AXES - PRECEDING ELEMENTS METHOD
#print("no of option elements:",len(option))                           # First we wrote the base element
                                                                      # Which is category (dropdown) element
                                                                      # Then we are calling all the option element
                                                                      # Through TAG-NAME <OPTION>
#4. Reading all option element
#Method1
#for opt in option:
#    print(opt.text)

#5. Selecting dropdown element without built-in method
for opt in option:
    op=opt.get_attribute('value')
    if op=='Art':
        op.click()
        break
time.sleep(4)

links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))

for link in links:
    url = link.get_attribute('href')
    response = requests.head(url)      # requests.head will send url to server from back-end & it won't click it.

    if response.status_code>=400:      # we will hit this url through </ request > and we will get response from browser.
        print(url,"Broken link")
    else:
        print(url,"Valid link")

driver.quit




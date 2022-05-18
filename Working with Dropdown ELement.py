from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)              # globally declaring imp_wait

driver.get("https://www.ebay.ca/")
print(driver.title)                     # title --> method
print(driver.current_url)               # current_url --> method

#1. HANDLING DROPDOWN ELEMENT:
# select() --> class is pre-requisite.
# we cannot access "DROPDOWN" element without it.

category = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select a category for search']"))
#category.click()                                    #click() fuction wont work with select

#2. There are 3 methods in "select" caleed as    < built in method >:
#category.select_by_visible_text("Automotive")       # <-- Most preferred method
category.select_by_index("3")                        # In html code --> count index code to get desired 'option' element
#category.select_by_value("6000")                    # give @attribute='value'


#3. Finding no. of option available:
#option = driver.find_elements(By.TAG_NAME,"option")
#print(len(option))
        # OR
# Another method is -->
option = category.options                  # "options" is --> method
print(len(option))                         # so we dont have to use locators

#4. How to Read all options:               # which return all option elements
#for opt in option:
#    print(opt.text)

#5. Select option from dropdown without built-in method:
#for opt in option:
#     if opt=='Automotive':
#        opt.click()
#        break

#6. How to handle dropdown when there is no < select > tag
op=driver.find_elements(By.XPATH,"//*[@id='gh-cat']/option")      #NOTE: </option> at last will select all option element
print("number of option element:",len(op))


driver.quit()




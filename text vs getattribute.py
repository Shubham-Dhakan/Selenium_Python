# TEST CASE:
# All application commands in selenium
# ALL conditional commands in selenium
# Difference b/w text vs get_attribute('value')
# How to print value through "text"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.ebay.ca/")
time.sleep(2)
driver.maximize_window()

# All application commands in selenium
print(driver.title)                                 #title
print(driver.current_url)                           #current_url
#print(driver.page_source)                          #page_source will give entire "html code" in o/p terminal (lengthy code)

# Difference b/w text vs get_attribute('value')
searchbox = driver.find_element(By.XPATH,"//input[@id='gh-ac']")
searchbox.send_keys("Apple Iphone 13 Pro")

print(searchbox.text)                       # NOTE: "TEXT" will only print element which has <inner text>.
print(searchbox.get_attribute('value'))     # NOTE: "get_attribute" will not print attribute value of link element.

# ALL conditional commands in selenium
print("display status:",searchbox.is_displayed())     # Only Conditional command needs webelement to execute them
print("enable status:",searchbox.is_enabled())        # "searchbox" is ---> < webelement >
print("selected status:",searchbox.is_selected())

# How to print value through "text"
sell = driver.find_element(By.LINK_TEXT,"Sell")       # "Sell" element has anchor tag
print(sell.text)                                      # so it will return <inner text> "sell" in o/p
print(sell.get_attribute('value'))                    #NOTE: get_attribute cannot print attribute value of
                                                      # web element which has anchor tag <//a>
                                                      # It will throw "none" in terminal instead of error.


# All Browser Commands
#driver.close()                                       #Only driver focused browser will get closed
#driver.quit()                                        #All browsers and kill back-end chrome driver process will get closed
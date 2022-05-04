from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.ebay.ca/")
time.sleep(2)
driver.maximize_window()

# ALL Application command
print(driver.title)                         # "title" is command
print(driver.current_url)                   # "current_url" is command
#print(driver.page_source)

# Locator Matching with single element
searchbox = driver.find_element(By.XPATH,"//input[@id='gh-ac']")
searchbox.send_keys("Apple Iphone 13 Pro")

# All conditional command
print("display status:",searchbox.is_displayed())           # "display" command will check selected element is displayed or not
print("enable status:",searchbox.is_enabled())              # "enable" command will check selected element is enabled or not
print("selected status:",searchbox.is_selected())           # "selected" command usually selects radio bttn or check box

#Locator matching with multiple elements
footer = driver.find_element(By.XPATH,"//footer[@id='glbfooter']//a")
print(footer.text)

#Locator not matching with element
sell = driver.find_element(By.LINK_TEXT,"Sell")             #If "sell" is written as "se" then locator then locator
sell.click()                                                #cannot find webelement
time.sleep(3)                                               #it will throw nosuchelementexeception
driver.back()

#find_element - returns multiple webelements
#Locator matching with single element
searchbox = driver.find_elements(By.XPATH,"//input[@id='gh-ac']")
print(len(searchbox))                                       #1 element is only there with this xpath
#searchbox[0].send_keys("Apple iphone 13 pro")              # It will search all elements with this xpath

#Locator matching with multiple element
footer = driver.find_elements(By.XPATH,"//footer[@id='glbfooter']//a")
print(len(footer))                                          # 91 elements

#for ftr in footer:                                         # Using "for loop"
#    print(ftr.text)                                        # It will print all elements under "footer"

#Locator not matching with element
sell = driver.find_elements(By.LINK_TEXT,"Sel")             # "Sel" is not the right value of its element
print(len(sell))                                            # Still it will not throw nosuchelementexception error
                                                            # Instead it will give show "0" in o/p terminal  

driver.quit()

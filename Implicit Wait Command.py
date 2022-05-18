from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)                  # <------ Addressing it "GLOBALLY" , because < IMPLICIT_WAIT > will identify
                                            # In script which element of < WEBPAGE > is having syncronisation issue.
                                            # It will not wait 10 seconds before locatiing every element
                                            # Waits at problem only
driver.get("https://www.ebay.ca/")
print(driver.title)                         # title is method
print(driver.current_url)                   # < current_url, page_source > are methods

searchbox = driver.find_element(By.XPATH,"//input[@id='gh-ac']")

searchbox.send_keys("Apple Iphone 13 Pro")
print(searchbox.get_attribute('value'))
searchbox.submit()                          # "submit()" is element method

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
myweb = WebDriverWait(driver,10)      # seconds

driver.get("https://www.ebay.ca/")
print(driver.title)                   # title is method
print(driver.current_url)             # current_url is method
#print(driver.page_source)            # page_source is method

# Find element with "explicit wait"
searchbox = myweb.until(EC.presence_of_element_located((By.XPATH,"//input[@id='gh-ac']")))
searchbox.send_keys("Apple Iphone 13 Pro")
searchbox.submit()                    # "submit" is element method, which reduces the length of code
                                      # Using submit(), we dont have to locate search button

driver.quit()
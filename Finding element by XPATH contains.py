from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.ebay.ca/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()

#1. Finding element through contains function
Searchbox = driver.find_element(By.XPATH,"//input[contains(@type,'te')]").send_keys("nike air force 1")
Searchbutton = driver.find_element(By.XPATH,"//input[contains(@type,'sub')]")
Searchbutton.click()
time.sleep(3)

#2. Finding element through contains(text) function
ebaydeals = driver.find_element(By.XPATH,"//a[contains(text(),' eBay Deals')]")
ebaydeals.click()
time.sleep(3)  


driver.quit()
#TEST CASE:
#1.Find elements by Relative XPATH with "OR" operator
#2.Find elements by Relative XPATH with "AND" operator

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.ebay.ca/")
print(driver.title)
print(driver.current_url)
time.sleep(5)

#1.Find elements by Relative XPATH with "OR" operator
# In "OR" operator anyone attribute should be same as given in html code.
#Homegarden = driver.find_element(By.XPATH,"//*[@id='mainContent' or @_sp='p2481888.m1385.l3250']/div[1]/ul/li[9]/a")
#Homegarden.click()
#time.sleep(5)

#2.Find elements by Relative XPATH with "AND" operator
# In "AND" operator both attributes should be same as given in html code or else it will not work.
searchbox = driver.find_element(By.XPATH,"//*[@type='text' and @id='gh-ac']").send_keys("nike air force 1")
button = driver.find_element(By.XPATH,"//*[@type='submit' and @id='gh-btn']")
button.click()
time.sleep(2)

nikeairforce = driver.find_element(By.XPATH,"//*")

driver.close

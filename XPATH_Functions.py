from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.ca/")
print(driver.title)
print(driver.current_url)

#1 Finding element through "CONTAINS" function - XPATH
driver.find_element(By.XPATH,"//*[@id='nav-link-accountList']").click()
Email = driver.find_element(By.XPATH,"//*[contains(@type,'ema')]").send_keys("----") # enter email id in send_keys
Continue = driver.find_element(By.XPATH,"//*[@id='continue']")
Continue.click()

Password = driver.find_element(By.XPATH,"//*[contains(@type,'password')]").send_keys("---") # enter password in send_keys
Signin = driver.find_element(By.XPATH,"//input[@id='signInSubmit']")
Signin.click()
time.sleep(5)

#contains only works with link, not sure but as per practical on-hand seems so.
#Password = driver.find_element(By.XPATH,"//input[contains(text(),'password')]").send_keys("Fordmustang@12")
#Siginin = driver.find_element(By.XPATH,"//input[contains(text(),'signInSubmit')]")
#Siginin.click()


driver.quit()

#Test Case:
#1. Finding element by absolute XPATH
#Randomly used class locator to find element
#2. Finding Element by Relative XPATH
#3. Navigating to the specific product by absolute XPATH

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.ebay.ca/")
print(driver.title)
print(driver.current_url)
time.sleep(5)

#1. Finding element by absolute XPATH
#input = driver.find_element(By.XPATH,"html/body/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[1]/div[1]/div/input[1]").send_keys("nike air force 1")
#button = driver.find_element(By.XPATH,"/html/body/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[3]/input")
#button.click()
#time.sleep(5)

#Randomly used class locator to find element
#driver.find_element(By.CLASS_NAME,"s-item__title.s-item__title--with-icon").click()

#2. Finding Element by Relative XPATH
input = driver.find_element(By.XPATH,"//input[@type='text']").send_keys("nike air force 1")
button = driver.find_element(By.XPATH,"//input[@value='Search']")
button.click()
time.sleep(2)

#3. Navigating to the specific product by absolute XPATH
#nikeairforce1 = driver.find_element(By.XPATH,"/html/body/div[5]/div[5]/div[2]/div[1]/div[2]/ul/li[1]/div/div[2]/a/h3")
#nikeairforce1.click()
#time.sleep(5)

#4. Navigating to the specific product by RELATIVE XPATH
nikeairforce1 = driver.find_element(By.XPATH,"//*[@id='srp-river-results']/ul/li[1]/div/div[2]/a/h3")
nikeairforce1.click()



driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
print(driver.title)
print(driver.current_url)

#1. Finding ELE by "CONTAINS"
searchbox = driver.find_element(By.XPATH,"//input[contains(@id,'sea')]").send_keys("tera mera rishta purana")
button = driver.find_element(By.XPATH,"//button[contains(@id,'acy')]")
button.click()

time.sleep(2)
driver.quit()

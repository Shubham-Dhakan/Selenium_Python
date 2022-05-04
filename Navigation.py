from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\Hp\\PycharmProjects\\SeleniumPython\\Drivers\\chromedriver.exe")

driver.get("http://www.scotiabank.com/")

print(driver.title)

time.sleep(5)

driver.get("http://www.Ford.com/")

print(driver.title)

time.sleep(5)

driver.back()

print(driver.title)

time.sleep(5)

driver.forward()

print(driver.title)

driver.quit()
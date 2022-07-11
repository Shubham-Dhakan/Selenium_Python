from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
import time
import os

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.honda.ca")
#First Method to get Screenshot
driver.save_screenshot("C:\\Users\\Shubham Dhakan\\PycharmProjects\\SeleniumPython\\Day 19\\homepage.png")

#Second Method:
#driver.get_screenshot_as_file(os.getcwd()+\\"homepage.png")

# < OS > has < getcwd() > current working directory feature
# Benefit: We dont have to write full path.
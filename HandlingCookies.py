from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)           # declaring globally so it applies to all elements where required

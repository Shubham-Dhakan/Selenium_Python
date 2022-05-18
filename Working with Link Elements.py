from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests as requests


driver = webdriver.Chrome()
driver.implicitly_wait(10)                      # Implicit Wait
mywait = WebDriverWait(driver,10)               # Explicit Wait

driver.get("https://www.ebay.ca/")
print(driver.title)
print(driver.current_url)
time.sleep(2)

links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))

for link in links:
    url = link.get_attribute('href')
    response = requests.head(url)      # requests.head will send url to server from back-end & it won't click it.

    if response.status_code>=400:      # we will hit this url through </ request > and we will get response from browser.
        print(url,"Broken link")
    else:
        print(url,"Valid link")

driver.quit()



#Test Case:
#Call all the packages
#1. Open Webbrowser
#2. Get URL
#3. Get Webpage title
#4. Get Current Url
#5. Maximize Window
#6. Finding element by Link_Test and CSS_SELECTOR Tag | Class
#7. Finding element by X_PATH
#8 Finding element by CSS_Selector Tag | Attribute
#8 Finding element by CSS_Selector Tag | class | Attribute
#9. Close

#Packages
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#1.Open Webbrowser
driver = webdriver.Chrome()

#2Get Url
driver.get("https://www.flipkart.com/")

#3.Get Webpage title
print(driver.title)

#4.Get Current Url
print(driver.current_url)
time.sleep(5)

#5.Maximize Window
driver.maximize_window()

#6.Finding element by Link_Test and CSS_SELECTOR Tag | Class
driver.find_element(By.LINK_TEXT,"Login").click()
driver.find_element(By.CSS_SELECTOR,"input._2IX_2-.VJZDxU").send_keys("---------")          # enter your email in send_keys
driver.find_element(By.CSS_SELECTOR,"input._2IX_2-._3mctLh.VJZDxU").send_keys("-------")    # enter your password in send_keys 

#7.Finding element by X_PATH
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").click()
time.sleep(5)

#8 Finding element by CSS_Selector Tag | Attribute
#driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search for products, brands and more']").send_keys("iphone 13 pro max")

#9 Finding element by CSS_Selector Tag | class | Attribute
driver.find_element(By.CSS_SELECTOR,"input._3704LK[type='text']").send_keys("iphone 13 pro max")
driver.find_element(By.CSS_SELECTOR,"svg").click()

time.sleep(10)

#9.Close
driver.close()






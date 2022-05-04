#Test Case:
#1. Open Web Browser (Chrome/Firefox/Internet Explorer)
#2. Open Url http://
#3. Provide Email
#4. Provide Password
#5. Click on login
#6. Finding element by Base(self) node
#7. Finding element by "PARENT" node
#8. Ancestor node
#9. Descendant node
#10. Following node
#11. Following-Siblings
#12. Preceding node
#13. Preceding-following Node

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

#2.Open Url http://
driver.get("https://www.amazon.ca/")
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH,"//*[@id='nav-link-accountList']").click()

#3,4,5 Provide Email, Provide Password, Click on login
driver.find_element(By.ID,"ap_email").send_keys("---")              # enter email in send_keys
driver.find_element(By.ID,"continue").click()
driver.find_element(By.NAME,"password").send_keys("---")            # enter password in send_keys
driver.find_element(By.ID,"auth-signin-button").click()

#6. Finding element by Base(self) node
#driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").click()

#7. Finding element by "PARENT" node
parent = driver.find_element(By.XPATH,"//input[@name='field-keywords']/parent::div[1]").click()

#8. Ancestor node
ans = driver.find_elements(By.XPATH,"//input[@name='field-keywords']/ancestor::div[2]")
print("number of ancestor node",len(ans))

#9. Descendant node
descendant = driver.find_elements(By.XPATH,"//input[@name='field-keywords']/ancestor::div[2]/descendant::*")
print("number of descendant nodes:",len(descendant))

#10. Following node
following = driver.find_elements(By.XPATH,"//input[@name='field-keywords']/ancestor::div[2]/following::*")
print("number of following nodes:",len(following))

#11. Following-Siblings
followingsiblings = driver.find_elements(By.XPATH,"//input[@name='field-keywords']/ancestor::div[2]/following-sibling::*")
print("number of following-siblings:",len(followingsiblings))

#12. Preceding node
preceding = driver.find_elements(By.XPATH,"//input[@name='field-keywords']/ancestor::div[2]/preceding::*")
print("number of preceding nodes:",len(preceding))

#13. Preceding-following Node
precedingsibling = driver.find_elements(By.XPATH,"//input[@name='field-keywords']/ancestor::div[2]/preceding-sibling::*")
print("number of precedingsibling node:",len(precedingsibling))

driver.close()

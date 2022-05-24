from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
import time

driver = webdriver.Chrome()
driver.maximize_window()            #maximize window

driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
print(driver.current_url)
wd=driver.current_window_handle            #Returns --> Window ID
print(wd)                                  #Returns --> Window ID

#1 Identifying Login Elements
username = driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
password = driver.find_element(By.NAME,"txtPassword").send_keys("admin123")
login = driver.find_element(By.ID,"btnLogin").click()

#2 Finding Elements dashboard --> admin --> usermanagement --> users
Admin = driver.find_element(By.XPATH,"//*[@id='menu_admin_viewAdminModule']/b").click()
UserManagement = driver.find_element(By.XPATH,"//*[@id='menu_admin_UserManagement']").click()
#Users = driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']").click()

#3 Locating Table
table = driver.find_element(By.XPATH,"//table[@id='resultTable']")
rows = len(driver.find_elements(By.XPATH,"//table[@id='resultTable']//tbody/tr"))
print("total number of rows in table:",rows)

count=0
for r in range(1,rows+1):
    data = driver.find_element(By.XPATH,"//table[@id='resultTable']//tbody/tr["+str(r)+"]/td[3]")
    if data=="ESS":
        count=count+1

print("total number of users:",rows)
print("Total number of ESS users:",count)
#print("Non ESS Users:",(rows-count))

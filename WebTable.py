#1 Count specific number of rows and columns
#2 Read Specific row and column data
#3 Read all row and all column

from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://testautomationpractice.blogspot.com/")
#driver.implicitly_wait(5)                   #implicit wait --> global declaration
#mywait = WebDriverWait(driver,5)            #explicit wait --> global declaration

print(driver.title)                          #title --> method
print(driver.current_url)                    #current_url --> method
driver.maximize_window()

#1 Count specific number of rows and columns
#noOFROWS=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
#noOFCOLUMNS=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))

#print(noOFROWS)        #7 rows
#print(noOFCOLUMNS)     #4 columns

#2 Read Specific row and column data
row_column_data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[2]")
#print(row_column_data.text)

#3 Read all row and all column
noOFROWS=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
noOFCOLUMNS=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/th"))

for r in range(2,noOFROWS+1):
    for c in range(1,noOFCOLUMNS+1):
        row_column_data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(row_column_data,end= "     ")         # <end = " "> gives output in table in form
    print()

driver.close()

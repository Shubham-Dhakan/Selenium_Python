from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()                # maximizes_window

driver.get("http://testautomationpractice.blogspot.com/")
driver.implicitly_wait(5)              # < implicit wait > declared gloablly

#1 Handling Alert Pop-up
click_button = driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()
myalert = driver.switch_to.alert
print(myalert.text)
myalert.accept()                        #accept() will close pop-up with < okay > option
#myalert.dismiss()                      #dismiss() will close ppo-up with < cancel > option

#2 Read Data on based of condition(List books name whose author name is " AMIT ")

noOFROWS=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/td"))
#noOFCOLUMNS=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print(noOFROWS)

for r in range(2,noOFROWS+1):
    authorname = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if authorname=="Amit":
        bookname = driver.find_element(By.XPATH,"table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        bookprice = driver.find_element(By.XPATH,"table[@name='BookTable']//tr["+str(r)+"]/td[4]").text
        print(bookname, bookprice)
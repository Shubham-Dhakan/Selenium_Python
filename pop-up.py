# Test Case:
#1. Locatiing and Testing Radio Button:
#2. Handling Alerts/pop-ups:
#3. How to Accept the pop-up:
#4. How to Reject the Alert/pop-up

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
import time

driver = webdriver.Chrome()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")     # get --> method
print(driver.title)                     # title --> method
print(driver.current_url)               # current_url --> method

#1. Locatiing and Testing Radio Button:
radiobutton = driver.find_element(By.CSS_SELECTOR,"input#remember[type='checkbox']")   # Using CSS_SELECTOR
                                                                                       # with tag,id,attribute
# Testing Radiobutton:
if radiobutton.is_selected():                               # is_selected() will verify if button selected or not
    radiobutton.click()
print("selected status:",radiobutton.is_selected())         # print will throw status of button selected or not
                                                            # in o/p terminal

#2. Handling Alerts/pop-ups:
driver.find_element(By.CSS_SELECTOR,"input.signinbtn[type='submit']").click()   # Using CSS_SELECTOR
                                                                                # with tag,class,attribute

Alert = driver.switch_to.alert              # switch_to.alert --> command (Pre-requisite)
                                            # Alert/Pop-up on webpage is not element
                                            # So it is Untrackable

#3. How to print Alert/pop-up prompt Text:
print(Alert.text)                           # This will print alert message of pop-up window
time.sleep(5)

#3. How to Accept the pop-up
#Alert.accept()                              # It will close pop-up window with <accept> option
                                            # To use accept() command we need object (pre-requisite)

#4. How to Reject the Alert/pop-up          # < ALERT > is our "object"
Alert.dismiss()                             # It will close pop-up window with <cancel> option
                                            # To use dismiss() command we need object (pre-requisite)

driver.quit()                               # Closes all browser and Kills back-end Chrome browser process.

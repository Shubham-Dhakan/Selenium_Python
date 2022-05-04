# TEST CASE:
#1. Approach1 "clicking all boxes"
#2. Approach2 "clicking all boxes"
#3. Approach3 "select multiple boxes of choice"
#4. Approach4 "select last two boxes out of 6 boxes"
#5. Approach5 "select first two boxes of 6 boxes"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()

#mywait = WebDriverWait(driver,10)          #Creating Explicit Wait
driver.implicitly_wait(10)                  #Creating Implicit Wait # Declaring it at top ---> so applies to entire script
                                            #where syncronisation problem is present

driver.get("https://www.ironspider.ca/forms/checkradio.htm")
driver.maximize_window()                    #Maximizes driver focused browser
print(driver.title)                         #Title is method
print(driver.current_url)                   #Current_Url is method

# Verify's specific boxes are selected by XPATH:
checkbox = driver.find_elements(By.XPATH,"//input[@name='color']")      #Find_elements Used because of list of elements
print(len(checkbox))                                                    #len will return total elements ---> 6

#1. Approach1 "clicking all boxes"
#for i in range(len(checkbox)):             #len(checkbox) will return length of checkbox element
#    checkbox[i].click()                    # "for loop" will click all boxes through "range(len(checkbox)"

#2. Approach2 "clicking all boxes"
#for chckbox in checkbox:                   #checkbox is returning list of elements
#    chckbox.click()                        #"for loop" itself will recognise no. of list elements returning and click all

#3. Approach3 "select multiple boxes of choice"
#for chckbox in checkbox:
#    color=chckbox.get_attribute('value')    # 'value' will return color name
#    if color=='red' or color=='blue':       # now through "if" loop it will click when 'value' will return 'red & blue'
#        chckbox.click()                     # if no such elements are located by <find_elements> then o/p -----> 0
                                             # but no exception error

#4. Approach4 "select last two boxes out of 6 boxes"
#for i in range(len(checkbox)-2,len(checkbox)):      # len(checkbox)-2 will give starting index --> 4, len(checkbox) is 6
#   checkbox[i].click()                              # len(checkbox) will give ending index --> 6
                                                     # return elements --> 5,6
#5. Approach5 "select first two boxes of 6 boxes"
#for i in range(len(checkbox)):                       # len(checkbox) returns 6 elements
#    if i<2:                                          # if loop will consider&click first 2 elements
#        checkbox[i].click()

#6. Approach6 Clearing all checkboxes
for chckbox in checkbox:
    chckbox.click()
    print("selected status:", chckbox.is_selected())  #over here it will pass "TRUE" value because selected

    if chckbox.is_selected():                         # "is_selected" will check that boxes are selected or not
            chckbox.click()                           # if selected than it will pass true value
                                                      # and click again which will clear boxes.

print("selected status:", chckbox.is_selected())      # over here it will pass "FALSE" value because "NOT" selected
driver.quit()
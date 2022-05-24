from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)           # implicit wait

driver.get("https://demoqa.com/")
driver.maximize_window()

print(driver.title)                 # title --> method
print(driver.current_url)           # current_url --> method

#leftpannel=driver.find_element(By.CLASS_NAME,"left-pannel")    # Locating Elements to reach frame
#leftpannel.click()

driver.find_element(By.XPATH,"//body/div[@id='app']/div[@class='body-height']/div[@class='home-content']/div[@class='home-body']/div[@class='category-cards']/div[1]").submit()

#frameeg = driver.find_elements(By.CSS_SELECTOR,"li#item-2.btn.btn-light")
#frameeg.click()




#frameeg=driver.find_element(By.XPATH,"//*[@id='item-2']/span")  # Locating Elements to reach frame
#frameeg.click()

#driver.switch_to.frame("frame1")                           # switiched to frame with ID
#print(heading.text)

#driver.switch_to.default_content()                         # Goes back to main webpage

#driver.switch_to.frame("frame2")
#message = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/iframe")
#print(message.text)
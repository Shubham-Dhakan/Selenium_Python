from selenium import webdriver
from selenium.webdriver.common.service import Service

ops = webdriver.ChromeOptions()                  #Through this we can have access of ChromeBrowser <settings>
#ops.add_argument("--disable notifications")      #This command will disable notification pop_up

driver = webdriver.Chrome()
driver.get("http://whatmylocation.com/")
driver.maximize_window()

driver.close()
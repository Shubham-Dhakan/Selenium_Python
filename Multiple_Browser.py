from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\Hp\\PycharmProjects\\SeleniumPython\\Drivers\\chromedriver.exe")
car = webdriver.Chrome(executable_path="C:\\Users\\Hp\\PycharmProjects\\SeleniumPython\\Drivers\\chromedriver.exe")
#driver = webdriver.Ie(executable_path="C:\\Users\\Hp\\Downloads\\IEDriverServer_Win32_4.0.0\\IEDriverServer.exe")
driver.get("http://www.scotiabank.com/")
car.get("http://www.honda.com/")
print(driver.title)
print(car.title)
print(car.current_url)
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='enter-scotiabank-canada']/span[2]").click()
time.sleep(10)
driver.quit()

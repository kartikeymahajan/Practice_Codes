from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
import time


print("sample test case started") 

# Using the Chrome webdriver
driver = webdriver.Chrome()

#maximize the window size  
driver.maximize_window()

#navigate to the url 
driver.get("https://www.google.com")

#identify the Google search text box and enter the value
driver.find_element(By.NAME, "q").send_keys("msys")

time.sleep(5)

#click on the Google search button
driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)

time.sleep(5)

driver.find_element(By.CSS_SELECTOR,"div.tF2Cxc a").click()

time.sleep(5)

print("Test executed successfully")

#close the browser  
driver.close()




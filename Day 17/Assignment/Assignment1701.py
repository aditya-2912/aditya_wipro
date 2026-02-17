from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://letcode.in/forms")
time.sleep(3)

# firstname
driver.find_element(By.ID,"firstname").send_keys("Aditya")

# lastname
driver.find_element(By.ID,"lasttname").send_keys("Raghuwanshi")

# email
driver.find_element(By.ID,"email").send_keys("test@gmail.com")

time.sleep(3)

# checkbox
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()

time.sleep(2)

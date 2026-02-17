from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://letcode.in/alert")

time.sleep(2)

driver.find_element(By.ID, "accept").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

time.sleep(2)

driver.find_element(By.ID, "confirm").click()
alert = driver.switch_to.alert
print(alert.text)
alert.dismiss()

time.sleep(2)

driver.find_element(By.ID, "prompt").click()
alert = driver.switch_to.alert
alert.send_keys("Aditya Raghuwanshi")
print(alert.text)
alert.accept()

time.sleep(2)

result = driver.find_element(By.ID, "myName").text
print(result)

driver.quit()
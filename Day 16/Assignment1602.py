from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Edge()
driver.get("https://www.facebook.com/")
driver.maximize_window()
print("1st page title : ",driver.title)
time.sleep(3)


driver.find_element(By.LINK_TEXT, "Create new account").click()
print("2nd page title",driver.title)
time.sleep(3)

driver.back()
print("After backward title",driver.title)
time.sleep(3)

driver.forward()
print("After Forward title",driver.title)
time.sleep(3)

driver.refresh()
print("Page got refreshed")
time.sleep(3)
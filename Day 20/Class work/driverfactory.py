from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

GRIDURL = "http://192.168.31.67:4444"

def getdriver(browser):
    if browser == "chrome":
        options = Options()
    elif browser == "firefox":
        options = FirefoxOptions()
    else:
        raise ValueError("Browser not supported")

    driver = webdriver.Remote(
        command_executor=GRIDURL,
        options=options
    )

    driver.maximize_window()
    return driver


driver = getdriver("chrome")
driver.get("https://google.com")

print(driver.title)
time.sleep(5)
driver.quit()

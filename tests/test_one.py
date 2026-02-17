import time

from selenium import webdriver


def test_one():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com")
    time.sleep(3)
    link='https://www.google.com/'
    text='Google'
    time.sleep(5)
    assert driver.title.__eq__(text)
    assert driver.current_url==link
    driver.close()
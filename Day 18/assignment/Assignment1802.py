from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()
driver.maximize_window()

# =====================================
# Open iframe site
# =====================================
driver.get("https://the-internet.herokuapp.com/iframe")

wait = WebDriverWait(driver, 15)

# =====================================
# 1. Switch to iframe
# =====================================
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr")))

# now inside iframe
box = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))

# enter text (no clear needed)
box.send_keys("Hello inside iframe")
print("Text entered inside iframe")

# =====================================
# 2. Back to main page
# =====================================
driver.switch_to.default_content()
print("Switched back to main page")

# =====================================
# 3. Open new tab
# =====================================
driver.execute_script("window.open('https://www.google.com')")
time.sleep(2)

# =====================================
# 4. Switch windows and print titles
# =====================================
windows = driver.window_handles

parent = windows[0]
child = windows[1]

driver.switch_to.window(child)
print("Child title:", driver.title)

driver.switch_to.window(parent)
print("Parent title:", driver.title)

# =====================================
# 5. Close child and return
# =====================================
driver.switch_to.window(child)
driver.close()

driver.switch_to.window(parent)
print("Child closed, back to parent")

time.sleep(3)
driver.quit()
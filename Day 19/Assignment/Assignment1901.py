from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# =========================
# Setup Chrome Driver
# =========================
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open demo website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# =====================================================
# 1️⃣ IMPLICIT WAIT  (applies globally to all elements)
# =====================================================
driver.implicitly_wait(10)   # wait up to 10 sec for elements

print("Implicit wait applied (10 seconds)")

# =====================================================
# 2️⃣ EXPLICIT WAIT (wait until element clickable)
# =====================================================
try:
    wait = WebDriverWait(driver, 20)

    username = wait.until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )
    username.send_keys("Admin")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("admin123")

    login_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )

    print("Login button is clickable now")
    login_btn.click()

except Exception as e:
    print("Explicit wait error:", e)

# =====================================================
# 3️⃣ FLUENT WAIT (with polling interval)
# =====================================================
try:
    # Fluent wait → checks every 2 sec for 20 sec
    fluent_wait = WebDriverWait(driver, 20, poll_frequency=2,
                                ignored_exceptions=[Exception])

    dashboard = fluent_wait.until(
        EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )

    # =====================================================
    # 4️⃣ PRINT MESSAGE WHEN ELEMENT AVAILABLE
    # =====================================================
    print("✅ Element is available for interaction: Dashboard loaded")

except Exception as e:
    print("Fluent wait error:", e)

time.sleep(5)
driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch Chrome Browser
driver = webdriver.Chrome()

# Open Website
driver.get("https://practicetestautomation.com/practice-test-login/")

# Maximize Browser
driver.maximize_window()

# Enter Username
username = driver.find_element(By.ID, "username")
username.send_keys("student")

# Enter Password
password = driver.find_element(By.ID, "password")
password.send_keys("Password123")

# Click Login Button
login_button = driver.find_element(By.ID, "submit")
login_button.click()

# Wait for page load
time.sleep(3)

# Validation
expected_text = "Logged In Successfully"

if expected_text in driver.page_source:
    print("Login Test Passed")
else:
    print("Login Test Failed")

# Close Browser
driver.quit()

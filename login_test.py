
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.maximize_window()

username = driver.find_element(By.ID, "username")
username.send_keys("student")

password = driver.find_element(By.ID, "password")
password.send_keys("Password123")

login_button = driver.find_element(By.ID, "submit")
login_button.click()

time.sleep(3)

expected_text = "Logged In Successfully"

if expected_text in driver.page_source:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.quit()

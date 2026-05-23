# signup_test.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://automationexercise.com/signup")

driver.maximize_window()

wait = WebDriverWait(driver, 10)

try:
    fullname = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='fullname']"))
    )
    fullname.send_keys("Sasidhar Palleni")

    
    email = driver.find_element(By.XPATH, "//input[@name='email']")
    email.send_keys("sasidhar@gmail.com")

    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("Test@123")

    confirm_password = driver.find_element(
        By.XPATH, "//input[@name='confirm_password']")
    confirm_password.send_keys("Test@123")

    signup_btn = driver.find_element(
        By.XPATH, "//button[text()='Sign Up']")
    signup_btn.click()
    
    success_msg = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'successful')]"))
    )

    print("Signup Test Passed")

except Exception as e:
    print("Signup Test Failed")
    print("Error:", e)

finally:
    time.sleep(3)
    driver.quit()

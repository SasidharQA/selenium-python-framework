
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://automationexercise.com")
driver.maximize_window()

# Create wait object
wait = WebDriverWait(driver, 10)

# Click Signup/Login
wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    )
).click()

# Click Forgot Password
wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(),'Forgot your password?')]")
    )
).click()

# Enter email
wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@type='email']")
    )
).send_keys("test@gmail.com")

# Click Submit
wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Submit')]")
    )
).click()

print("Forgot Password Test Passed")

driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://automationexercise.com")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    )
).click()

wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(),'Forgot your password?')]")
    )
).click()

wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@type='email']")
    )
).send_keys("test@gmail.com")

wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Submit')]")
    )
).click()

print("Forgot Password Test Passed")

driver.quit()

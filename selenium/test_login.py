
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:5000")

    driver.find_element(By.ID, "username").send_keys("suruthi")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.ID, "loginButton").click()

    wait = WebDriverWait(driver, 10)
    wait.until(lambda d: d.find_element(By.ID, "message").text != "")

    message = driver.find_element(By.ID, "message").text
    print(message)

    assert message == "Login Successful"
    print("TEST PASSED")

finally:
    driver.quit()

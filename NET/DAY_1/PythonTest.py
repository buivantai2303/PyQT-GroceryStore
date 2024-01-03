from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("file:///C:/Users/BanhMiBietBay/Desktop/Front_End/5_DemoElement/NET/index.html")

    username_input = "sa"
    password_input = "sa"

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    username.clear()
    username.send_keys(username_input)
    password.clear()
    password.send_keys(password_input)

    driver.execute_script("login()")

    WebDriverWait(driver, 10).until(
        EC.url_changes("file:///C:/Users/BanhMiBietBay/Desktop/Front_End/5_DemoElement/NET/index.html")
    )

    if "TheBigCat" in driver.current_url:
        print("Login successful. Test passed.")
    else:
        print("Login failed. Test failed.")

finally:
    driver.quit()

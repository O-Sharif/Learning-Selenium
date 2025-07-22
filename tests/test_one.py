from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.CLASS_NAME,'username').send_keys("student")
driver.find_element(By.ID,'password').send_keys("Password123")
driver.find_element(By.ID, "submit").click()

driver.implicitly_wait(10)





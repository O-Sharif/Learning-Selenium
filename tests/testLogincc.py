
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def open_browser():
    driver = webdriver.Chrome()
    driver.get('https://callinsight.testdomains1.com/')
    sleep(10)
    return driver

def login(driver,email, password):
    driver.find_element(By.ID, 'email').send_keys(email)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    sleep(10)  # Wait for login to complete

def main():
    driver = open_browser()
    login(driver,"random@zvvzuv.com", "Pa$$w0rd!")
    print("Browser opened and closed successfully.")
    driver.quit()

if __name__ == "__main__": # This ensures the script runs only when executed directly
    main()




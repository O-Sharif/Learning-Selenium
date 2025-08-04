from random import choice
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


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
    from random import randint

def upload_new_call(driver):
    call_records = driver.find_element(By.XPATH,'//span[text()="Upload New Call"]')
    call_records.click()
    sleep(5)  # Wait for the page to load
    print("Upload New Call button clicked successfully.")

    today = datetime.now().strftime("%a %b %d %Y")
    call_name = f"Test Call - {today}"

    call_name_input = driver.find_element(By.ID, 'callName')
    call_name_input.clear()  # Clear any existing text in the input field
    sleep(2)  # Wait for the input field to be ready
    call_name_input.send_keys(call_name)
    sleep(5)

    agent_click_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Filter by agent"]')
    agent_click_button.click()
    sleep(5)

    first_option = driver.find_element(By.CSS_SELECTOR, 'div[id="radix-:r2c:"]')
    first_option.click()
    sleep(5)





def main():
    driver = open_browser()
    login(driver,"tike@bltiwd.com", "Pa$$w0rd!")
    print("Browser opened and closed successfully.")
    upload_new_call(driver)
    driver.quit()

if __name__ == "__main__": # This ensures the script runs only when executed directly
    main()




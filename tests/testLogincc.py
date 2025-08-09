

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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


def upload_new_call(driver, ):
    wait = WebDriverWait(driver, 10)

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

    #drop_down = driver.find_element(By.XPATH,"(//*[@role='combobox'])[1]")
    #drop_down.click()
    #sleep(2)

    drop_down = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@role='combobox'])[1]")))
    drop_down.click()

    search = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search agents...']")))
    search.clear()
    search.send_keys("iron")

    sleep(5)  # Wait for the search results to load
    option = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//*[@data-value='iron Hammer ironhammer1212@gmail.com none']"
    )))
    option.click()




def main():
    driver = open_browser()
    login(driver,"tike@bltiwd.com", "Pa$$w0rd!")
    print("Browser opened and closed successfully.")
    upload_new_call(driver)
    driver.quit()

if __name__ == "__main__": # This ensures the script runs only when executed directly
    main()




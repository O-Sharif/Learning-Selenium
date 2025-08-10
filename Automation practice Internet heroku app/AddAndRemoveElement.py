from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def open_browser():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com")
    return driver
def navigate_to_add_remove_elements(driver):
    driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
    sleep(3)


def add_element(driver):
    driver.find_element(By.XPATH, "//button[text()='Add Element']").click()
    sleep(3)

def remove_element(driver):
    driver.find_element(By.CLASS_NAME, "added-manually").click()
    sleep(3)

def main():
    driver = open_browser()
    sleep(5)
    driver.maximize_window()
    add_element(driver)
    remove_element(driver)
    sleep(3)
    driver.quit()

if __name__ == "__main__":
    main()

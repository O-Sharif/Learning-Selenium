
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def open_browser():
    driver = webdriver.Chrome()
    driver.get('https://callinsight.testdomains1.com/')
    sleep(10)
    return driver








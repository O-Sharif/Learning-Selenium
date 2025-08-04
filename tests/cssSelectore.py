
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


def open_browser():
    driver = webdriver.Chrome()
    driver.get("https://automationpractice.qualitytestinghub.com/dropdown-list/")
    sleep(10)
    return driver

def main():
    driver = open_browser()
    driver.quit()
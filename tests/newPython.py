from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get('https://mental-health-check-nine.vercel.app/')
sleep(10)
button = driver.find_element(By.XPATH,"//button[@class='justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-10 px-4 py-2 flex items-center gap-2']")
button.click()
sleep(10)

driver.find_element(By.ID,"email").send_keys("irontester80@gmail.com")
driver.find_element(By.ID,"password").send_keys("12345678")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
sleep(10)
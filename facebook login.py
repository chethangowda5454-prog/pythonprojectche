from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(10)

driver.minimize_window()
time.sleep(10)
driver.maximize_window()
time.sleep(10)

driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Mahesh")

time.sleep(30)
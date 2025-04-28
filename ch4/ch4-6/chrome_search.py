from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://google.com')

el = driver.find_element(By.NAME, 'q')
el.send_keys('Pythonの教科書')
el.submit()

time.sleep(30)
driver.close()
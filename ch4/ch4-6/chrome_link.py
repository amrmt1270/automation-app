from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://uta.pw/sakusibbs/'
driver = webdriver.Chrome()
driver.get(url)

link = driver.find_element(By.LINK_TEXT, '名作アーカイブ')

link.click()
time.sleep(30)
driver.close()

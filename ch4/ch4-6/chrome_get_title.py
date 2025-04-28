from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'https://uta.pw/sakusibbs/post.php?mml_id=35'
driver.get(url)

time.sleep(10)
e = driver.find_element(By.CLASS_NAME, 'posttitle')
print(e.text)
driver.close()
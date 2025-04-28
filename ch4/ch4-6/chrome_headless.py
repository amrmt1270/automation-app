from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://uta.pw/sakusibbs/users.php?user_id=1'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options = options)

driver.get(url)
a_list = [driver.find_element(By.CSS_SELECTOR, 'ul#mmlist li a')]
for a in a_list:
    print('◾️', a.text)
    print(a.get_attribute('href'))

driver.close()
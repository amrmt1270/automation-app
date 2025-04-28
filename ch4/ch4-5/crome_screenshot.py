from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://python.org')
driver.save_screenshot('screenshot.png')
driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.XPATH, '/html/body/form/input[1]')
first_name.send_keys("Thanh")

last_name = driver.find_element(By.XPATH, '/html/body/form/input[2]')
last_name.send_keys("Nguyen")

email = driver.find_element(By.XPATH, '/html/body/form/input[3]')
email.send_keys("ThanhNguyen@gmail.com")

button = driver.find_element(By.XPATH, '/html/body/form/button')
button.click()

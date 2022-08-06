from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://tinder.com/")
time.sleep(2)
log_in = driver.find_element(By.XPATH, '//*[@id="q554704800"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.click()
time.sleep(2)
more_opt = driver.find_element(By.XPATH, '//*[@id="q-1173676276"]/div/div/div[1]/div/div/div[3]/span/button')
more_opt.click()
time.sleep(2)
log_in_gg = driver.find_element(By.XPATH, '//*[@id="q-1173676276"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
log_in_gg.click()
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
time.sleep(2)
email_address = driver.find_element(By.XPATH, '//*[@id="email"]')
email_address.send_keys("Your email")
time.sleep(2)
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.click()
password.send_keys("Your password")
password.send_keys(Keys.ENTER)
driver.switch_to.window(base_window)
time.sleep(10)
allow_locate = driver.find_element(By.XPATH, '//*[@id="q-1173676276"]/div/div/div/div/div[3]/button[1]/span')
allow_locate.click()
time.sleep(2)
noti_enable = driver.find_element(By.XPATH, '//*[@id="q-1173676276"]/div/div/div/div/div[3]/button[1]/span')
noti_enable.click()
time.sleep(2)
cookie_acpt = driver.find_element(By.XPATH, '//*[@id="q554704800"]/div/div[2]/div/div/div[1]/div[1]/button/span')
cookie_acpt.click()
time.sleep(10)
for i in range(100):
    try:
        like_button = driver.find_element(By.XPATH, '//*[@id="q554704800"]/div/div[1]/div/main/div[1]/div/div')
        like_button.send_keys(Keys.ARROW_LEFT)
    except NoSuchElementException:
        continue
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sign_in = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()
email_sign_in = driver.find_element(By.XPATH, '//*[@id="username"]')
email_sign_in.send_keys('******************')
password_sign_in = driver.find_element(By.XPATH, '//*[@id="password"]')
password_sign_in.send_keys('***********')
sign_in_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()
job_list = driver.find_elements(By.CSS_SELECTOR, "a .disabled ember-view job-card-container__link job-card-list__title")
for job in job_list:
    try:
        time.sleep(2)
        job.click()
        time.sleep(2)
        save_button = driver.find_element(By.CSS_SELECTOR, "button .jobs-save-button artdeco-button artdeco-button--3 artdeco-button--secondary")
        save_button.click()
    except NoSuchElementException:
        print("No save button, skipped.")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time 

SIMILAR_ACCOUNT = 'chefsteps'
IG_USERNAME = 'your email'
IG_PASSWORD = 'your password'


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)
        self.username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.username.send_keys(IG_USERNAME)
        time.sleep(2)
        self.password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.password.send_keys(IG_PASSWORD)
        self.password.send_keys(Keys.ENTER)
        time.sleep(5)
        self.save_lg_but = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
        self.save_lg_but.click()
        time.sleep(4)
        self.noti_but = self.driver.find_element(By.CSS_SELECTOR, '._a9--._a9_1')
        self.noti_but.click()
        time.sleep(2)

    def find_followers(self):
        self.search_bar = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input')
        self.search_bar.send_keys(SIMILAR_ACCOUNT)
        self.search_bar.click()
        time.sleep(1)
        self.search_bar.send_keys(Keys.ENTER)
        self.search_bar.send_keys(Keys.ENTER)
        time.sleep(10)

    def follow(self):
        self.followers_pop_up = self.driver.find_element(By.CSS_SELECTOR, '._ac2a')
        self.followers_pop_up.click()
        time.sleep(2)
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, '._acan._acap._acas')
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
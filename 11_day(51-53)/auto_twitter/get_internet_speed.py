from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = 'your mail'
TWITTER_USERNAME = 'your id'
TWITTER_PASSWORD = 'your password'


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.up = 0
        self.down = 0

    def twitter_login(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://twitter.com/")
        time.sleep(3)
        self.sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')
        self.sign_in_button.click()
        time.sleep(4)
        self.sign_in_email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        self.sign_in_email.send_keys(TWITTER_EMAIL)
        self.sign_in_email.send_keys(Keys.ENTER)
        time.sleep(3)
        self.sign_in_username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        self.sign_in_username.send_keys(TWITTER_USERNAME)
        self.sign_in_username.send_keys(Keys.ENTER)
        time.sleep(2)
        self.sign_in_password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        self.sign_in_password.send_keys(TWITTER_PASSWORD)
        self.sign_in_password.send_keys(Keys.ENTER)
        time.sleep(200)

    def get_internet_speed(self):
        time.sleep(2)
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        self.go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.go_button.click()
        time.sleep(100)
        self.down_info = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down = float(self.down_info.text)
        self.up_info = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = float(self.up_info.text)
        return [self.up, self.down]

    def tweet_at_provider(self, a: list):
        self.twitter_post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span')
        self.twitter_post.send_keys(f"Hey, why my internet speed {a[1]}down/{a[0]}up when I pay for 150down/10up?")
        time.sleep(5)
        self.post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        self.post_button.click()
        time.sleep(20)
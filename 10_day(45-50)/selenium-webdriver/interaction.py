from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://en.wikipedia.org/wiki/Main_Page/")

article_cnt = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# article_cnt.click()
# print(article_cnt.text)

link_text = driver.find_element(By.LINK_TEXT, "Herman the Arch­deacon")
# link_text.click()

search = driver.find_element(By.XPATH, '//*[@id="searchInput"]')
search.send_keys("Python")
search.send_keys(Keys.ENTER)
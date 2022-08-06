from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org/")

events = {}

list_length = len(driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')) 
# Can copy the xpath by right click on the element and choose copy then Xpath
# Use the get_attribute("...") to get the thing you want.
for i in range(1, list_length+1):
    time = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time').text
    name = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a').text
    events[i] = {
        "time": f"{time}",
        "name": f"{name}",
    }

print(events)
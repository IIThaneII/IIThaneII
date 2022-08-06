from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://orteil.dashnet.org/experiments/cookie/") 

continue_game = 1
while continue_game == 1:
    try:
        cookie_clicker = driver.find_element(By.XPATH, '//*[@id="cookie"]')
        cookie_clicker.click()

        crursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b')
        grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b')
        factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b')
        mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]/b')
        shipment = driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b')
        alchemy_lab = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b')
        portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]/b')
        time_machine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b')
        upgrade_list = [crursor, grandma, factory, mine, shipment, alchemy_lab, portal, time_machine]
        money_list = [int(n.text.split(" - ")[1].replace(",","")) for n in upgrade_list]
        money = int(driver.find_element(By.XPATH, '//*[@id="money"]').text)

        if money > min(money_list):
            i = money_list.index(min(money_list))
            upgrade_list[i].click()
    except StaleElementReferenceException:
        continue

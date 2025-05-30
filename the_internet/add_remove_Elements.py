from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/")

add_remove = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[2]/a')
add_remove.click()

add = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
add.click()

remove = driver.find_element(By.CSS_SELECTOR, 'button[class="added-manually"]')
remove.click()

time.sleep(2)
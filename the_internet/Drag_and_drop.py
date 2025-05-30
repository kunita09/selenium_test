from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/")

drag_and_drop = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[10]/a')
drag_and_drop.click()

col_a = driver.find_element(By.ID, "column-a")
col_b = driver.find_element(By.ID, "column-b")

action_chains = ActionChains(driver)

action_chains.drag_and_drop(col_a, col_b).perform()
action_chains.drag_and_drop(col_b, col_a).perform()

time.sleep(2)
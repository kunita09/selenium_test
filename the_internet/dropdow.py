from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/")

page = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[11]/a')
page.click()

dropdow = driver.find_element(By.ID, "dropdown")
dropdow.click()

option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="dropdown"]/option[2]'))
)
# option = driver.find_element(By.XPATH, '//*[@id="dropdown"]/option[2]')
option.click()

time.sleep(5)




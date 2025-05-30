from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# สร้าง Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# เปิดเว็บไซต์
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# รอจน input username พร้อมใช้งาน
input_user = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Username"]'))
)
input_user.send_keys("Admin")

input_pass = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Password"]'))
)
input_pass.send_keys("admin123")

login = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
login.click()

# search = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search"]'))
# )
# search.send_keys("info")

# info = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a')
info = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a'))
)
info.click()

edit_fname = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, 'firstName'))
)
# input[placeholder="First Name"]
edit_fname.click()
edit_fname.clear()
edit_fname.clear()
# edit_fname.send_keys("newton")

time.sleep(5)
# browser_setup.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    # คืนค่าตัวแปร driver ที่พร้อมใช้งาน
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

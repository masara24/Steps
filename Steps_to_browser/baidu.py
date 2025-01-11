from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
#chromedriver.exe same location with this file
service = Service("chromedriver.exe")
options = Options()

# exe
options.binary_location = r"..\chrome-win64\chrome-win64\chrome.exe"

print("can i make baidu?")
# headless
# options.add_argument("--headless") 

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
#options.add_argument('--start-maximized')
options.add_argument('--no-sandbox')  # fix:DevToolsActivePort file doesn't exist
options.add_argument('--disable-gpu')  # fix:DevToolsActivePort file doesn't exist
options.add_argument('--disable-dev-shm-usage')  # fix:DevToolsActivePort file doesn't exist
options.add_argument('--remote-debugging-port=9222')  # fix:DevToolsActivePort file doesn't

driver = webdriver.Chrome(service=service, options=options)

url = "https://www.baidu.com/"
driver.get(url)
driver.quit()
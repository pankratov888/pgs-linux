import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys



# Установка прав на исполняемый файл ChromeDriver
chromedriver_path = ChromeDriverManager().install()
os.chmod(chromedriver_path, 0o755)

chrome_options = Options()
chrome_options.add_argument("--headless=new")

service = ChromeService(chromedriver_path)
driver = webdriver.Chrome(options=chrome_options, service=service)

wait = WebDriverWait(driver, 10)

print("Открытие страницы...")
driver.get("https://demo.knd.gov.ru")
print("Страница загружена.")

# Вывод HTML страницы для отладки
print(browser.page_source)

# Закрыть браузер
driver.quit()

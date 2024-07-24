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

binary_yandex_driver_file = r'./bin/yandexdriver'
os.chmod(binary_yandex_driver_file, 0o755)  # Сделать файл исполняемым
# Путь к расширению
#extension_path = './extensions/1.2.13_0.crx'
#if not os.path.isfile(extension_path):
    #raise FileNotFoundError(f"Extension not found: {extension_path}")

#pem_path = './extensions/1.2.13_0.pem'

options = webdriver.ChromeOptions()

service = ChromeService(executable_path=binary_yandex_driver_file)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
options.add_argument('--headless')
logs = driver.get_log('browser')
network_logs = driver.get_log("browser")
current_url = driver.current_url





print("Запуск браузера...")
driver = webdriver.Chrome(service=service, options=options)
print("Браузер запущен успешно.")

print("Открытие страницы...")
driver.get("https://ya.ru")
print("Страница загружена.")


# Закрыть браузер
driver.quit()

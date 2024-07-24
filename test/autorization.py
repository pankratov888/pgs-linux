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
from pyvirtualdisplay import Display

# Start virtual display
display = Display(visible=0, size=(1920, 1080))
display.start()

binary_yandex_driver_file = r'./bin/chromedriver' # path to YandexDriver
# Дать права на выполнение файла yandexdriver
os.chmod(binary_yandex_driver_file, 0o755)

options = webdriver.ChromeOptions()

service = ChromeService(executable_path=binary_yandex_driver_file)
driver = webdriver.Chrome(service=service)

print("Открытие страницы...")
driver.get("https://auth.pgs.gosuslugi.ru/auth/realms/DigitalgovTorkndProd1Auth/protocol/openid-connect/auth?client_id=DigitalgovTorkndProd1Auth-Proxy&state=b6fa62fc48c9м04787fa5bf095da2bafa&nonce=8bf3d529b0af28816d18e97bf560c4d3&response_type=code&redirect_uri=https%3A%2F%2Fpgs.gosuslugi.ru%2Fopenid-connect-auth%2Fredirect_uri&scope=openid")
print("Страница загружена.")
# Вывод HTML страницы для отладки
print(driver.page_source)
# Закрыть браузер
driver.quit()

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

binary_yandex_driver_file = r'./bin/yandexdriver'
os.chmod(binary_yandex_driver_file, 0o755)  # Сделать файл исполняемым
# Путь к расширению
extension_path = './extensions/1.2.13_0.crx'
#if not os.path.isfile(extension_path):
    #raise FileNotFoundError(f"Extension not found: {extension_path}")

pem_path = './extensions/1.2.13_0.pem'

# Настройки Chrome

options = webdriver.ChromeOptions()
service = ChromeService(executable_path=binary_yandex_driver_file)
driver = webdriver.Chrome(service=service, options=options)

options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")
options.add_extension(extension_path)
options.add_argument(f'--ssl-client-cert={pem_path}')

# Включение логирования в Chrome
options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})



try:
    print("Запуск браузера...")
    driver = webdriver.Chrome(service=service, options=options)
    print("Браузер запущен успешно.")

    print("Открытие страницы...")
    driver.get("https://auth.psi.pgs.gosuslugi.ru/auth/realms/DigitalgovTorkndPsiAuth/protocol/openid-connect/auth?client_id=DigitalgovTorkndPsiAuth-Proxy&nonce=aa9422a9cfe770cdc50b7b5ef6af9005&state=bf4730d94618c5333d91b7949555208a&redirect_uri=https%3A%2F%2Fpsi.pgs.gosuslugi.ru%2Fopenid-connect-auth%2Fredirect_uri&scope=openid%20email&response_type=code")
    print("Страница загружена.")

finally:
    # Закрыть браузер
    driver.quit()

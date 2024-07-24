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

# Установка прав на исполняемый файл ChromeDriver
chromedriver_path = ChromeDriverManager().install()
os.chmod(chromedriver_path, 0o755)

# Путь к расширению
extension_path = './extensions/1.2.13_0.crx'
if not os.path.isfile(extension_path):
    raise FileNotFoundError(f"Extension not found: {extension_path}")

pem_path = './extensions/1.2.13_0.pem'

# Настройки Chrome
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")
options.add_extension(extension_path)
options.add_argument(f'--ssl-client-cert={pem_path}')

# Включение логирования в Chrome
options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

# Инициализация веб-драйвера
service = ChromeService(executable_path=chromedriver_path)
browser = None

try:
    print("Запуск браузера...")
    browser = webdriver.Chrome(service=service, options=options)
    print("Браузер запущен успешно.")

    print("Открытие страницы...")
    browser.get("https://auth.psi.pgs.gosuslugi.ru/auth/realms/DigitalgovTorkndPsiAuth/protocol/openid-connect/auth?client_id=DigitalgovTorkndPsiAuth-Proxy&nonce=aa9422a9cfe770cdc50b7b5ef6af9005&state=bf4730d94618c5333d91b7949555208a&redirect_uri=https%3A%2F%2Fpsi.pgs.gosuslugi.ru%2Fopenid-connect-auth%2Fredirect_uri&scope=openid%20email&response_type=code")
    print("Страница загружена.")

finally:
    # Закрыть браузер
    browser.quit()

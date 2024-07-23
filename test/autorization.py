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

# Настройки Chrome
options = Options()
options.add_argument("--headless")  # Отключить режим headless для отладки
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Добавление расширения
options.add_extension(extension_path)

# Включение логирования в Chrome
options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

# Инициализация веб-драйвера
service = ChromeService(executable_path=chromedriver_path)
browser = webdriver.Chrome(service=service, options=options)

try:
    print("Открытие страницы...")
    browser.get("https://auth.psi.pgs.gosuslugi.ru/auth/realms/DigitalgovTorkndPsiAuth/protocol/openid-connect/auth?client_id=DigitalgovTorkndPsiAuth-Proxy&nonce=aa9422a9cfe770cdc50b7b5ef6af9005&state=bf4730d94618c5333d91b7949555208a&redirect_uri=https%3A%2F%2Fpsi.pgs.gosuslugi.ru%2Fopenid-connect-auth%2Fredirect_uri&scope=openid%20email&response_type=code")
    print("Страница загружена.")

    # Найти поле поиска
    search_box = browser.find_element(By.NAME, 'text')  # Поле поиска на Яндекс имеет имя 'text'

    # Ввести текст в поле поиска
    search_text = 'Привет, мир!'
    search_box.send_keys(search_text)

    # Проверка, что текст введен
    entered_text = search_box.get_attribute('value')
    if entered_text == search_text:
        print("Текст успешно введен в поле поиска.")
    else:
        print("Ошибка: введенный текст не совпадает с ожидаемым.")

    # Нажать кнопку поиска (обычно это кнопка с типом submit или может быть отдельная кнопка)
    search_box.send_keys(Keys.RETURN)  # Нажать Enter для отправки формы

    # Немного подождать, чтобы увидеть результаты поиска
    time.sleep(3)  # Подождите 3 секунды (можно настроить время ожидания в зависимости от скорости вашего соединения)

finally:
    # Закрыть браузер
    browser.quit()

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

# Настройки Chrome
options = Options()
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Включение логирования в Chrome
options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

# Инициализация веб-драйвера
service = ChromeService(chromedriver_path)
browser = webdriver.Chrome(service=service, options=options)

try:
    print("Открытие страницы...")
    browser.get("http://ya.ru")
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

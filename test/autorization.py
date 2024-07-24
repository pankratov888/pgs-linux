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

binary_yandex_driver_file = r'./bin/yandexdriver' # path to YandexDriver
# Дать права на выполнение файла yandexdriver
os.chmod(binary_yandex_driver_file, 0o755)

options = webdriver.ChromeOptions()

service = ChromeService(executable_path=binary_yandex_driver_file)
driver = webdriver.Chrome(service=service)

print("Открытие страницы...")
driver.get("http://ya.ru")
print("Страница загружена.")
# Найти поле поиска
search_box = driver.find_element(By.NAME, 'text')  # Поле поиска на Яндекс имеет имя 'text'

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

# Закрыть браузер
driver.quit()

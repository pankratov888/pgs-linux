from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Путь к исполняемому файлу Chrome
chrome_path = r'D:\a\test_all\test_all\bin\chromium-gost\chromium-gost-49.0.2623.112-win32\chrome.exe'


# Настройки Chrome
options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = chrome_path  # Укажите путь к исполняемому файлу Chrome

# Инициализация веб-драйвера
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

try:
    print("Открытие страницы...")
    browser.get("http://ya.ru")
    print("Страница загружена.")

    # Вывод HTML страницы для отладки
    print(browser.page_source)

    # Проверка наличия элемента по атрибуту data-hydration-id
    hydration_id = "576211ff6da7ce6ac7272570289f34fc.0"
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"[data-hydration-id='{hydration_id}']")))
    print("Элемент отображается на странице.")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    browser.quit()

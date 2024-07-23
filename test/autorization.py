import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Включение логирования в Chrome
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['goog:loggingPrefs'] = {'browser': 'ALL'}

# Установка прав на исполняемый файл ChromeDriver
chromedriver_path = ChromeDriverManager().install()
os.chmod(chromedriver_path, 0o755)

# Настройки Chrome
options = Options()
# Убираем опцию безголового режима
# options.add_argument("--headless")

# Оставляем другие полезные опции
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Инициализация веб-драйвера
service = ChromeService(chromedriver_path)
browser = webdriver.Chrome(service=service, options=options, desired_capabilities=capabilities)

try:
    print("Открытие страницы...")
    browser.get("http://ya.ru")
    print("Страница загружена.")

    time.sleep(3)

    # Проверка наличия элемента по атрибуту data-hydration-id
    hydration_id = "5190d93cc2f5a9bf0738b7c6faa01986.0"
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"[data-hydration-id='{hydration_id}']")))
    print("Элемент отображается на странице.")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    browser.quit()
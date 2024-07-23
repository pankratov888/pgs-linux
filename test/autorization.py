import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Настройки Chrome
options = Options()
#options.add_argument("--headless")

# Укажите путь к вашему chromedriver для Windows
chromedriver_path = "./bin/chromedriver"

# Создайте сервис с указанием пути к chromedriver
service = Service(chromedriver_path)

# Создайте экземпляр браузера с использованием сервиса
driver = webdriver.Chrome(service=service)

try:
    print("Открытие страницы...")
    driver.get("http://ya.ru")
    print("Страница загружена.")

    time.sleep(3)

    # Проверка наличия элемента по атрибуту data-hydration-id
    hydration_id = "5190d93cc2f5a9bf0738b7c6faa01986.0"
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"[data-hydration-id='{hydration_id}']")))
    print("Элемент отображается на странице.")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()

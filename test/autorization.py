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
from selenium.common.exceptions import TimeoutException



# Установка прав на исполняемый файл ChromeDriver
chromedriver_path = ChromeDriverManager().install()
os.chmod(chromedriver_path, 0o755)

chrome_options = Options()
chrome_options.add_argument("--headless=new")

service = ChromeService(chromedriver_path)
driver = webdriver.Chrome(options=chrome_options, service=service)



print("Открытие страницы...")
driver.get("https://demo.knd.gov.ru")
print("Страница загружена.")
wait = WebDriverWait(driver, 30)

try:
    # Ищем элемент "Вход через ЕСИА" по CSS-селектору
    esia_login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > app-root > evolenta-login > div > div.login-wrapper > div > div")))

    # Клик по элементу
    esia_login_button.click()
    print("Элемент найден и нажат.")
except TimeoutException:
    print("Ошибка: элемент не найден в течение заданного времени ожидания.")
    # Сохранение скриншота для отладки
    driver.save_screenshot('screenshot.png')
    print("Скриншот сохранен как 'screenshot.png'.")

# Активация, заполнение поля Логин
input_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#login")))
input_field.click()
input_field.send_keys("+79374426231")

# Активация, заполнение поля Пароль
input_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#password")))
input_field.click()
input_field.send_keys("S.pank470")

# Нажимаем кнопку "Войти"
login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > esia-root > div > esia-login > div > div.form-container.disable-outline > form > div:nth-child(4) > button")))
login_button.click()

# Открываем сервис генерации TOTP-кодов в новом окне
driver.execute_script("window.open('https://piellardj.github.io/totp-generator/?secret=AFDQSZB3NFBUCTBRSUEZ6NWCQIWCR66S&digits=6&period=30&algorithm=SHA-1')")
driver.switch_to.window(driver.window_handles[1])
# Находим и копируем код
copy_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#copy-generated-code")))
copy_button.click()
time.sleep(1)
# Переходим обратно в первое окно
driver.switch_to.window(driver.window_handles[0])
# Вставляем скопированный код в поле ввода на странице авторизации
code_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > esia-root > div > esia-login > div > div > esia-enter-mfa > esia-ttp > form > div.input-control > div > esia-code-input > div > code-input > span:nth-child(1)")))
code_input.click()
time.sleep(1)
code_input.send_keys(Keys.CONTROL + 'v')  # Вставляем скопированный код
# Задержка перед переходом на следующую страницу
time.sleep(5)  # Подождать 5 секунд, чтобы страница загрузилась


# Закрыть браузер
driver.quit()

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



# Установка прав на исполняемый файл ChromeDriver
chromedriver_path = ChromeDriverManager().install()
os.chmod(chromedriver_path, 0o755)

# Настройки Chrome
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Включение логирования в Chrome
options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

# Инициализация веб-драйвера
service = ChromeService(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)


print("Открытие страницы...")
driver.get("https://demo.knd.gov.ru/login")
print("Страница загружена.")
time.sleep(5)

# Нажимаем кнопку "Вход через ЕСИА"
esia_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/evolenta-login/div/div[2]/div/div")))
esia_button.click()
# Ждем, чтобы страница ЕСИА загрузилась
driver.implicitly_wait(2)
# Активация поля ввода телефона и ввод телефона
login_input = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/esia-root/div/esia-login/div/div[1]/form/div[1]/esia-input/input")))
login_input = driver.find_element("xpath", "/html/body/esia-root/div/esia-login/div/div[1]/form/div[1]/esia-input/input")
login_input.click()  # Активация поля ввода
time.sleep(2)
login_input.send_keys("+79374426231")  # Ввод телефона
# Активация поля ввода пароля и ввод пароля
login_input = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/esia-root/div/esia-login/div/div[1]/form/div[2]/esia-input-password/div/input")))
password_input = driver.find_element("xpath", "/html/body/esia-root/div/esia-login/div/div[1]/form/div[2]/esia-input-password/div/input")
password_input.click()  # Активация поля ввода
time.sleep(2)
password_input.send_keys("S.pank470")  # Ввод пароля
# Нажимаем кнопку "Войти"
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/esia-root/div/esia-login/div/div[1]/form/div[4]/button")))
login_button.click()
# Открываем сервис генерации TOTP-кодов в новом окне
driver.execute_script("window.open('https://piellardj.github.io/totp-generator/?secret=AFDQSZB3NFBUCTBRSUEZ6NWCQIWCR66S&digits=6&period=30&algorithm=SHA-1')")
driver.switch_to.window(driver.window_handles[1])
# Находим и копируем код
copy_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[3]/div/div[2]/div[1]/button")))
copy_button.click()
time.sleep(1)
# Переходим обратно в первое окно
driver.switch_to.window(driver.window_handles[0])
# Вставляем скопированный код в поле ввода на странице авторизации
code_input = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/esia-root/div/esia-login/div/div/esia-enter-mfa/esia-ttp/form/div[2]/div/esia-code-input/div/code-input/span[1]/input")))
code_input.click()
time.sleep(1)
code_input.send_keys(Keys.CONTROL + 'v')  # Вставляем скопированный код
# Задержка перед переходом на следующую страницу
time.sleep(5)  # Подождать 5 секунд, чтобы страница загрузилась
driver.refresh()
# Нажимаем кнопку "Далее"
next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/evolenta-select-branch/div/div[2]/div[2]/div/div/div[2]")))
next_button.click()
# Ждем, пока страница загрузится
time.sleep(5)  # Подождать 5 секунд


# Закрыть браузер
driver.quit()

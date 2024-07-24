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

binary_yandex_driver_file = r'./bin/chromedriver' # path to YandexDriver
# Дать права на выполнение файла yandexdriver
os.chmod(binary_yandex_driver_file, 0o755)

options = webdriver.ChromeOptions()


service = ChromeService(executable_path=binary_yandex_driver_file)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

print("Открытие страницы...")
driver.get("https://auth.pgs.gosuslugi.ru/auth/realms/DigitalgovTorkndProd1Auth/protocol/openid-connect/auth?client_id=DigitalgovTorkndProd1Auth-Proxy&state=b6fa62fc48c9м04787fa5bf095da2bafa&nonce=8bf3d529b0af28816d18e97bf560c4d3&response_type=code&redirect_uri=https%3A%2F%2Fpgs.gosuslugi.ru%2Fopenid-connect-auth%2Fredirect_uri&scope=openid")
print("Страница загружена.")
time.sleep(5)
# Нажимаем кнопку "Вход через ЕСИА"
esia_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='kc-social-providers']/ul")))
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
next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/form/div/button[2]/div")))
next_button.click()
# Ждем, пока страница загрузится
time.sleep(5)  # Подождать 5 секунд


# Закрыть браузер
driver.quit()

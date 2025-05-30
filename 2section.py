from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Создаем временный текстовый файл (если его нет)
file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "file.txt")
with open(file_path, 'w') as file:
    file.write("")  # Создаем пустой файл

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнение текстовых полей
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("test@example.com")
    
    # Загрузка файла
    browser.find_element(By.ID, "file").send_keys(file_path)
    
    # Нажатие кнопки Submit
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # Получение результата из alert
    time.sleep(1)  # Даем время для появления alert
    alert = browser.switch_to.alert
    result = alert.text.split()[-1]  # Извлекаем число из текста alert
    print("Результат:", result)
    alert.accept()

finally:
    time.sleep(3)
    browser.quit()
    # Удаление временного файла (опционально)
    os.remove(file_path)
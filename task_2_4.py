from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
from math import log, sin
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

try:
    # Автоматическая установка драйвера
    service = Service(GeckoDriverManager().install())

    # Настройки Firefox
    options = Options()
    options.headless = False

    # Создаем браузер
    browser = webdriver.Firefox(service=service, options=options)

    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажать на кнопку "Book"
    button = browser.find_element(By.ID, "book")
    button.click()

    # Решить математическую задачу
    value = browser.find_element(By.ID, "input_value").text
    value = int(value)
    result = str(log(abs(12 * sin(value))))

    # Ввести ответ
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(result)

    # Нажать на кнопку "Submit"
    button = browser.find_element(By.ID, "solve")
    button.click()

    # Получить результат из alert
    time.sleep(1)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print("Ответ:", alert_text.split()[-1])
    alert.accept()
except:
    time.sleep(2)
    browser.quit()

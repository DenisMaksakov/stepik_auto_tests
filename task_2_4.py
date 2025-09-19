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
except:
    pass

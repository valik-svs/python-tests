from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
book_btn = '#book'
price = '#price'
num1 = 'input_value'
ansver = '#answer'
submit_btn = 'button[type="submit"]'
num1 = 'input_value'



# ждём понижения цены
WebDriverWait(browser, 20).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, price),
        "$100")
)
browser.find_element_by_css_selector(book_btn).click()


el1 = browser.find_element_by_id(num1)
element1 = el1.text
result = math.log(abs(12*math.sin(int(element1))))
ansver = browser.find_element_by_css_selector(ansver)
ansver.send_keys(str(result))
browser.find_element_by_css_selector(submit_btn).click()

# Завершаем бронирование



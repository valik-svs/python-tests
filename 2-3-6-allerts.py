from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
from selenium import webdriver
import math
import time


link = "http://suninjuly.github.io/alert_accept.html"

first_name = '[name="firstname"]'
last_name = '[name="lastname"]'
email = '[name="email"]'
file = '[name="file"]'
submit_btn = 'button[type="submit"]'
ansver = '#answer'
num1 = 'input_value'


try:
    browser = webdriver.Chrome()
    browser.get(link)
    #На первой странице находим и клацаем на кнопку
    submit_btn1 = browser.find_element_by_css_selector(submit_btn)
    submit_btn1.click()
    alert = browser.switch_to.alert
    alert.accept()
    #На следующе странице решаем задачку для прохождения теста

    el1 = browser.find_element_by_id(num1)
    element1 = el1.text
    result = math.log(abs(12 * math.sin(int(element1))))
    ansver = browser.find_element_by_css_selector(ansver)
    ansver.send_keys(str(result))
    submit_btn2 = browser.find_element_by_css_selector(submit_btn)
    submit_btn2.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
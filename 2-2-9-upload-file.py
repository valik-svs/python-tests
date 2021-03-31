from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
from selenium import webdriver


link = "http://suninjuly.github.io/file_input.html"

first_name = '[name="firstname"]'
last_name = '[name="lastname"]'
email = '[name="email"]'
file = '[name="file"]'
submit_btn = 'button[type="submit"]'



try:
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    first_name = browser.find_element_by_css_selector(first_name)
    last_name = browser.find_element_by_css_selector(last_name)
    email = browser.find_element_by_css_selector(email)
    file = browser.find_element_by_css_selector(file)
    submit_btn = browser.find_element_by_css_selector(submit_btn)

    first_name.send_keys('some-name')
    last_name.send_keys('some-last-name')
    email.send_keys('some-email')
    file.send_keys(file_path)

    submit_btn.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
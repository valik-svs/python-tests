from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium import webdriver

link = "http://suninjuly.github.io/selects1.html"

num1 = 'num1'
num2 = 'num2'
dropdown = 'select#dropdown'
submit_btn = 'button[type="submit"]'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    el1 = browser.find_element_by_id('num1')
    element1 = el1.text
    el2 = browser.find_element_by_id('num2')
    element2 = el2.text
    select = Select(browser.find_element_by_css_selector(dropdown))
    result = int(element1)+int(element2)
    select.select_by_value(str(result))  # ищем элемент с текстом "Python"
    submit = browser.find_element_by_css_selector(submit_btn)


    browser = webdriver.Chrome()
    browser.execute_script("document.title='Script executing';alert('Robots at work');")
    #submit.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
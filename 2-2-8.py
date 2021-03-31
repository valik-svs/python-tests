from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import math
#(abs(12*sin(x))), where x = 166?

link = "https://SunInJuly.github.io/execute_script.html"


num1 = 'input_value'
submit_btn = 'button[type="submit"]'
ansver = '#answer'
checkbox = 'robotCheckbox'
radio_btn = "label[for='robotsRule']"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    el1 = browser.find_element_by_id(num1)
    element1 = el1.text
    result = math.log(abs(12*math.sin(int(element1))))
    input = browser.find_element_by_css_selector(ansver)
    robo_checkbox = browser.find_element_by_id(checkbox)
    input.send_keys(str(result))
    robo_checkbox.click()
    browser.execute_script("window.scrollBy(0, 100);")
    radio = browser.find_element_by_css_selector(radio_btn)
    radio.click()
    button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
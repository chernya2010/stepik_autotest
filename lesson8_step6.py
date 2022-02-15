from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
print(x_element)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(calc(x))

checkbox = browser.find_element_by_css_selector("#robotCheckbox")
checkbox.click()

radio = browser.find_element_by_css_selector("#robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()

button = browser.find_element_by_css_selector("body > div > form > button")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
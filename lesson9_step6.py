from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("body > form > div > div > button")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
print(x_element)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(calc(x))

button = browser.find_element_by_css_selector("body > form > div > div > button")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
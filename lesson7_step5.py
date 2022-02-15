from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector('#treasure')
print(x_element)
x = x_element.get_attribute("valuex")
print(x)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(calc(x))

checkbox = browser.find_element_by_css_selector("#robotCheckbox")
checkbox.click()

radio = browser.find_element_by_css_selector("#robotsRule")
radio.click()

submit = browser.find_element_by_css_selector("body > div > form > div > div > button")
submit.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(11)
# закрываем браузер после всех манипуляций
browser.quit()

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector('h2 > span:nth-of-type(2)')
x = x_element.text
print(x)
y_element = browser.find_element_by_css_selector('h2 > span:nth-of-type(4)')
y = y_element.text
print(y)


def calc(x, y):
    return str((int(x)) + (int(y)))


select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(calc(x, y))  # ищем элемент с нашей суммой

submit = browser.find_element_by_css_selector("form > .btn.btn-default")
submit.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(3)
# закрываем браузер после всех манипуляций
browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

value = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

button = browser.find_element_by_css_selector("#bookW")
button.click()

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
print(x_element)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(calc(x))

button = browser.find_element_by_css_selector("#solve")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
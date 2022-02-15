from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(2)")
first_name.send_keys("Alex")

last_name = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(4)")
last_name.send_keys("Chernya")

email = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(6)")
email.send_keys("chernya@mail.com")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "1.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element_by_css_selector("#file")
element.send_keys(file_path)

button = browser.find_element_by_css_selector("body > div > form > button")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
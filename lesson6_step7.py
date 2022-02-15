from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")
elements = browser.find_elements_by_tag_name("input")
for element in elements:
    element.send_keys("М1")

button = browser.find_element_by_css_selector("body > div > form > button")
button.click()

# не забываем оставить пустую строку в конце файла

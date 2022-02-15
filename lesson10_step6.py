from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")

button = browser.find_element_by_id("button")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
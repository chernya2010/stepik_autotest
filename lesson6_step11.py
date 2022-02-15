from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector(".first_block > .first_class.form-group > .first.form-control")
    input1.send_keys("Ivan")
    #input1 = browser.find_element_by_css_selector(".first_block > .form-group.second_class > .form-control.second")
    #input1.send_keys("Ivanov")
    input1 = browser.find_element_by_css_selector(".form-control.third")
    input1.send_keys("ivanov_ivan@mail.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("form[method='get'] > .btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
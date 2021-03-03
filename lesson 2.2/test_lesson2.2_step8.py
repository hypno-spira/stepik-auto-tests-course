from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_tag_name("input[name=firstname]")
    input1.send_keys("Alena")
    input2 = browser.find_element_by_tag_name("input[name=lastname]")
    input2.send_keys("Kotek")
    input3 = browser.find_element_by_tag_name("input[name=email]")
    input3.send_keys("hi@mail.ru")
    
    # получаем путь к директории текущего исполняемого скрипта lesson2_7.py
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # имя файла, который будем загружать на сайт
    file_name = "file.txt"
    # получаем путь к file_example.txt
    file_path = os.path.join(current_dir, file_name)
    # отправляем файл
    element = browser.find_element_by_css_selector("#file")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector(".btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
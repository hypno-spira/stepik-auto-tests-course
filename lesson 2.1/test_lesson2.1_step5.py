from selenium import webdriver
import math

link = "http://suninjuly.github.io/math.html"

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента.
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector(".form-control")
    input1.send_keys(y)

    checkBox1 = browser.find_element_by_id("robotCheckbox")
    checkBox1.click()

    radioButton1 = browser.find_element_by_id("robotsRule")
    radioButton1.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
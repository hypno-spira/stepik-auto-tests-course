from selenium import webdriver
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    xElement = browser.find_element_by_id("input_value")
    
    # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента.
    # xElementText = xElement.text
    
    x = int(xElement.text)
    y = calc(x)

    input1 = browser.find_element_by_css_selector(".form-control")
    input1.send_keys(y)

    checkBox1 = browser.find_element_by_id("robotCheckbox")
    checkBox1.click()

    radioButton1 = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radioButton1)
    radioButton1.click()

    button = browser.find_element_by_css_selector(".btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
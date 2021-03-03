from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    firstNumber = browser.find_element_by_id("num1")
    secondNumber = browser.find_element_by_id("num2")
    
    # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента.
    firstNumberText = firstNumber.text
    secondNumberText = secondNumber.text
    
    summa = int(firstNumberText) + int(secondNumberText)
    summaText = str(summa)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(summaText)

    button = browser.find_element_by_css_selector(".btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
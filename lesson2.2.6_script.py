from selenium import webdriver
import math
import time 

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_css_selector(".form-control")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)
    
    chb1 = browser.find_element_by_id("robotCheckbox")
    chb1.click()
    
    rb1 = browser.find_element_by_id("robotsRule")
    rb1.click()

    
    
    button = browser.find_element_by_css_selector(".btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()



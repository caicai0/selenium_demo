
import time
from selenium import webdriver
from selenium import common

def isElementExist(driver,element):
    flag=True
    browser=driver
    try:
        browser.find_element_by_css_selector(element)
        return flag

    except:
        flag=False
        return flag

f = open('/Users/liyufeng/Desktop/baidu.txt')
text = f.read()
f.close()

browser = webdriver.Firefox()
browser.get('http://www.baidu.com')
time.sleep(2)
login_button = browser.find_element_by_link_text('登录')
login_button.click()
time.sleep(0.3)
user_login_button = browser.find_element_by_css_selector('#TANGRAM__PSP_10__footerULoginBtn')
user_login_button.click()
time.sleep(0.3)

input_username = browser.find_element_by_css_selector('#TANGRAM__PSP_10__userName')
input_username.send_keys('采采01')
input_password = browser.find_element_by_css_selector('#TANGRAM__PSP_10__password')
input_password.send_keys('BAIdu791008.')
submit = browser.find_element_by_css_selector('#TANGRAM__PSP_10__submit')
submit.click()
time.sleep(0.3)
context = browser.context()

lines = text.split('\n')
for line in lines :
    arr = line.split(',')
    link = arr[0]
    password = arr[1]
    browser.get(link)
    browser.set_context(context)
    time.sleep(3)
    password_input = browser.find_element_by_css_selector('input.QKKaIE.LxgeIt')
    password_input.send_keys(password)
    button = browser.find_element_by_css_selector('.g-button')
    button.click()
    time.sleep(1)
    select = browser.find_element_by_css_selector('.QAfdwP > li:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
    select.click()

    save_btn = browser.find_element_by_css_selector('.g-button-blue > span:nth-child(1) > em:nth-child(1)')
    save_btn.click()
    time.sleep(0.4)


    time.sleep(100000000)
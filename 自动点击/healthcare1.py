
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

#登录页面
browser = webdriver.Firefox()
browser.get('http://www.cn-healthcare.com/freezing/')
time.sleep(2)
name = browser.find_element_by_css_selector("input.placeholder-no-fix")
name.send_keys('admin')
password = browser.find_element_by_name("password")
password.send_keys('ZgjkjCn2016')
submit = browser.find_element_by_css_selector('button.btn.green.pull-right')
submit.click()
time.sleep(1.5)

# #管理页面
huiyuan_title = browser.find_element_by_link_text("系统管理")
huiyuan_title.click()
time.sleep(0.5)
shenhe_tile = browser.find_element_by_link_text("用户管理")
shenhe_tile.click()
time.sleep(0.6)

def onePage():
    for i in range(1,10) :
        box = browser.find_element_by_css_selector('#tbody > tr:nth-child(6) > td:nth-child('+str(i)+') > input:nth-child(1)')
        box.click()

        change = browser.find_element_by_css_selector('button.btn:nth-child(2)')
        change.click()
        

for i in range(1,35) :
    pageInput = browser.find_element_by_name('PageNumber')

    pageInput.clear()
    browser.switch_to.alert.accept()

    time.sleep(1)
    pageInput.send_keys(str(i))
    time.sleep(0.3)
    jump = browser.find_element_by_link_text("转到")
    jump.click()
    time.sleep(0.7)





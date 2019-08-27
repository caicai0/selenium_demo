
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

#管理页面
huiyuan_title = browser.find_element_by_link_text("会员管理")
huiyuan_title.click()
time.sleep(0.5)
shenhe_tile = browser.find_element_by_link_text("认证用户审核")
shenhe_tile.click()

# 扫描元素
while True :
    # 通过
    if isElementExist(browser,'.breadcrumb > shiro\:haspermission:nth-child(1) > button:nth-child(1)') :
        tong = browser.find_element_by_css_selector('.breadcrumb > shiro\:haspermission:nth-child(1) > button:nth-child(1)')
        if tong.is_displayed() :
            tong.click()

    # 忽略
    # if isElementExist(browser,'.breadcrumb > shiro\:haspermission:nth-child(1) > button:nth-child(2)') :
    #     nextBtn = browser.find_element_by_css_selector('.breadcrumb > shiro\:haspermission:nth-child(1) > button:nth-child(2)')
    #     if nextBtn.is_displayed():
    #         nextBtn.click()

    if isElementExist(browser,'#nextshow > div:nth-child(3) > a:nth-child(1)') :
        nextBtn = browser.find_element_by_css_selector('#nextshow > div:nth-child(3) > a:nth-child(1)')
        if nextBtn.is_displayed():
            nextBtn.click()



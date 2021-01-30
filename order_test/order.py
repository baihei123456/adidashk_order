# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
#import unittest
def order():
    driver = webdriver.Chrome("E:\study\Chrome\Application\chromedriver.exe")
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("https://uat-www.etc-parts.com/#/login")
    driver.find_element_by_name("loginName").send_keys("18888888123")
    driver.find_element_by_name("password").send_keys("Aa123456")
    driver.find_element_by_css_selector('.el-button.login-in.el-button--primary').click()
    time.sleep(5)
    # print(member_info)
    driver.find_element_by_class_name('shopingCar-icon').click()
    time.sleep(1)
    driver.find_element_by_class_name('el-icon-minus').click()
order()
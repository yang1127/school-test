'''
# coding = utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()
time.sleep(3)
browser.get("http://www.baidu.com")
time.sleep(3)
browser.find_element_by_id("kw").send_keys("selenium")
time.sleep(3)
browser.find_element_by_id("su").click()
browser.quit()



#coding=utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get("http://www.baidu.com")

#百度输入框定位

#通过id 方式定位
browser.find_element_by_id("kw").send_keys("selenium")

#通过name 方式定位
browser.find_element_by_name("wd").send_keys("selenium")

#通过tag name 方式定位 -> 不能成功，因为input太多了不唯一
browser.find_element_by_tag_name("input").send_keys("selenium")

#通过class name 方式定位
browser.find_element_by_class_name("s_ipt").send_keys("selenium")

#通过CSS 方式定位
browser.find_element_by_css_selector("#kw").send_keys("selenium")

#通过xphan 方式定位
browser.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")

browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()


#coding=utf-8
from selenium import webdriver
browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
browser.find_element_by_link_text("hao123").click()
browser.quit()

#coding=utf-8
from selenium import webdriver
browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
browser.find_element_by_link_text("hao123").click()
browser.quit()

'''

#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
time.sleep(2)

driver.find_element_by_id("kw").send_keys("test")
time.sleep(2)

driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(2)

#通过submit() 来操作
driver.find_element_by_id("su").submit()

time.sleep(3)
driver.quit()
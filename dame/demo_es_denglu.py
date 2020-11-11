import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
#打开浏览器登录页面
driver.get('http://192.168.4.223/upload/')
driver.implicitly_wait(10)#隐式等待
time.sleep(2)

#验证码处理
driver.add_cookie({'name':'ECS[password]','value':'20c801b5e8531a40a6ecc4903af30708'})
driver.add_cookie({'name':'ECS[user_id]','value':'37'})
driver.add_cookie({'name':'ECS[username]','value':'admin3'})
driver.add_cookie({'name':'ECS[visit_times]','value':'1'})
driver.add_cookie({'name':'ECS_ID','value':'d02e377be002ee60415a61b54c0996d90a9c458a'})
#刷新
# driver.refresh()
driver.get('http://192.168.4.223/upload/')

# #登录
# driver.find_element_by_link_text('登录').click()
# time.sleep(2)
# #输入
# driver.find_element_by_name("username").send_keys('admin3')
# driver.find_element_by_name("password").send_keys('LS514320ls')
# driver.find_element_by_name("remember").click()
# driver.find_element_by_name("submit").click()
# driver.implicitly_wait(10)#隐式等待
# driver.find_element_by_link_text('女装').click()
# driver.find_element_by_partial_link_text('秋冬').click()
# driver.find_element_by_xpath('//*[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img').click()
#进入详细页面，定位尺寸元素位置，点击
#定位数量输入框，输入购买量
#定位立即购买按钮位置，点击



time.sleep(5)
driver.quit()
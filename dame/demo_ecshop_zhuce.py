#有问题
import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
#打开浏览器登录页面
driver.get('http://192.168.4.223/upload/')
driver.implicitly_wait(10)#隐式等待
time.sleep(2)
#注册
driver.find_element_by_link_text('注册').click()
driver.implicitly_wait(10)#隐式等待
#输入
driver.find_element_by_name("username").send_keys('ysss')
driver.find_element_by_name("email").send_keys('120537114@qq.com')
driver.find_element_by_name("password").send_keys('yss123321')
driver.find_element_by_name("confirm_password").send_keys('yss123321')
driver.find_element_by_name("extend_field1").send_keys('120537114@qq.com')
driver.find_element_by_name("extend_field2").send_keys('123321')
driver.find_element_by_name("extend_field3").send_keys('123321')
driver.find_element_by_name("extend_field4").send_keys('15928561321')
driver.find_element_by_name("extend_field5").send_keys('15928561321')
question=driver.find_element_by_name("sel_question")
xuanzeqi=Select(question)
xuanzeqi.select_by_index(1)
driver.find_element_by_name("passwd_answer").send_keys('2020')
#提交
driver.find_element_by_name("Submit").click()
time.sleep(5)
driver.quit()
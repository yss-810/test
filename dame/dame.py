import time#引入时间模块
from selenium import webdriver#引入webdriver
driver = webdriver.Chrome()#启动chrome浏览器，实例化driver对象
driver.maximize_window()#最大化浏览器窗口
# driver.set_window_size(480,700)设置窗口大小
# driver.minimize_window()窗口最小化
driver.get("http://www.baidu.com")#打开浏览器并访问网页
driver.back()#后退一步
time.sleep(3)#强制等待
driver.forward()#前进一步
driver.get("http://www.taobao.com")
time.sleep(2)#强制等待
driver.refresh()
time.sleep(3)#强制等待
driver.get("http://www.jd.com")
time.sleep(3)#强制等待
# driver.close()#关闭浏览器
driver.quit()#关闭并退出
import time

import unittest

class BaiDuTestCase(unittest.TestCase):
    def setUp(self):
        print('开始')

        from selenium import webdriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_baidu(self):

        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(20)
        # 操作
        self.driver.find_element_by_id('kw').send_keys("python")
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        self.driver.find_element_by_partial_link_text('Python(计算机程序设计语言)_百度百科').click()
        time.sleep(5)
        title=self.driver.title
        self.assertIn("python",title)


    def test_baidu_search(self):

        # 访问
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_name('wd').send_keys("linux")
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        self.driver.find_element_by_name('wd').clear()
        time.sleep(1)
        self.driver.find_element_by_class_name('s_ipt').send_keys("自动化")
        self.driver.find_element_by_id('su').click()
        time.sleep(5)






    def tearDown(self):
        print('结束')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


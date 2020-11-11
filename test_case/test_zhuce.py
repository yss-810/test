import time
import unittest

from unittest import result

from selenium import webdriver

import driver
from driver.browser import chrome_browser
from lib.utils import read_excel
from page.zhuce_page import ZhucePage


class ZhuceTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = chrome_browser()

    def tearDown(self):
        self.driver.quit()

    def test_zhuce(self):
        zp=ZhucePage(self.driver)

        # content=read_excel()
        # print('读取成功',content)
        # uname = content[1][0]
        # email = content[1][1]
        # password = content[1][2]
        # mobile = content[1][3]



        result=zp.zhuce('yss9','1053741200@qq.com','yss123321','yss123321','120537114','15928561321')

        time.sleep(3)
        self.assertEqual("yss9", result)



if __name__ == '__main__':
    unittest.main()

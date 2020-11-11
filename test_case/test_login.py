import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from driver.browser import chrome_browser
from page.login_page import LoginPage


class LoginTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=chrome_browser()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login(self):
        lp = LoginPage(self.driver)
        result=lp.login('yss','yss123321')
        time.sleep(3)

        print(result)
        self.assertEqual('yss', result)


        # self.assertEqual('admin3', result)


if __name__ == '__main__':
    unittest.main()

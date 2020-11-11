import unittest

from selenium.webdriver.common.by import By


class CommodityaddTestCase(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver
        self.locator_ele_commodity_management=(By.XPATH, ('//ul[@id="menu-ul"]/li[1]'))
        self.locator_ele_add_goods=(By.LINK_TEXT,('添加新商品'))


    def ele_switchframe(self):
        pass

    def ele_commodity_management(self):
        self.driver.find_element(*self.locator_ele_commodity_management).click()

    def ele_add_goods(self):
        self.driver.find_element(self.locator_ele_add_goods).click()

    def ele_switchparent(self):
        pass

    def ele_switchframe1(self):
        pass

    def ele_

























        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

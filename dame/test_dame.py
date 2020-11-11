import unittest
class Dame_a(unittest.TestCase):
    def setUp(self):
        print("开始")
    def test_A(self):
        print("A用例")
    def test_B(self):
        print("用例B")
    def test_C(self):
        print("用例C")
    def tearDown(sel):
        print("结束")
if __name__ == '__main__':
    unittest.main()



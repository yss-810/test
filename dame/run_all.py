import unittest
from HTMLTestRunner import HTMLTestRunner

#批量匹配用例
discover=unittest.defaultTestLoader.discover(start_dir="../", pattern='test*.py')

# runner=unittest.TextTestRunner()
# runner.run(discover)
#执行用例生成报告
with open("report.html", "wb")as file:

    runner=HTMLTestRunner(stream=file,     #注意缩进
                          description="自动化测试报告详情",
                          title="ECShop自动化测试报告")
    runner.run(discover)
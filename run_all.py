import unittest
from HTMLTestRunner import HTMLTestRunner

discover=unittest.defaultTestLoader.discover(start_dir='test_case',
                                    pattern='test*.py',
                                    top_level_dir=None)
report_path='report/'+'report.html'
with open(report_path,'wb')as file:
    runner=HTMLTestRunner(
        stream=file,
        title='自动化测试报告-登录',
        description='报告详情'
    )
    runner.run(discover)
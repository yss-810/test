import unittest

from dame.test_dame import Dame_a
from dame.test_dame_baidu_sreach import BaiDuTestCase

suite=unittest.TestSuite()
suite.addTest(BaiDuTestCase("test_baidu_search"))
suite.addTest(Dame_a("test_A"))

runner=unittest.TextTestRunner()
runner.run(suite)



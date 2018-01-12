import unittest

from selenium import webdriver


class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.FF = webdriver.Firefox()

    def testSearch(self):
        self.FF.get("https://www.baidu.com")

    def tearDown(self):
        self.FF.quit()


if __name__ == '__main__':
    unittest.main()

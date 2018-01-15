import unittest
import HTMLTestRunner

import time

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.readYaml import ReadYaml
from utils import location


class TestIntranet(unittest.TestCase):
    url = ReadYaml(location.CONFIG_FILE).yaml_data()['URL']
    phone_number = (By.XPATH, '//*[@id="login-form"]/fieldset/label[1]/span/input')
    password = (By.XPATH, '//*[@id="login-form"]/fieldset/label[2]/span/input')
    login_btn = (By.XPATH, '//*[@id="login-form"]/fieldset/button')

    def setUp(self):
        self.FF = webdriver.Chrome()
        self.FF.get(self.url)

    def testSearch(self):
        self.FF.find_element(*self.phone_number).clear()
        self.FF.find_element(*self.phone_number).send_keys('15102100358')
        self.FF.find_element(*self.password).clear()
        self.FF.find_element(*self.password).send_keys('123456')
        self.FF.find_element(*self.login_btn).click()
        time.sleep(5)

    def tearDown(self):
        self.FF.quit()


if __name__ == '__main__':
    test_unit = unittest.TestSuite()
    now = time.strftime('%Y%m%d%H%M', time.localtime())
    print(location.REPORT_PATH)
    f = open(os.path.join(location.REPORT_PATH, 'report_' + now + '.html'), 'w', encoding='utf-8')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=u'测试报告', description='')
    test_unit.addTest(TestIntranet('testSearch'))
    runner.run(test_unit)
    f.close()

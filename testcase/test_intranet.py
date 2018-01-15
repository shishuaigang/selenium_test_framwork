import unittest
import HTMLTestRunner

import time

import os
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from utils.readYaml import ReadYaml
from utils import location
from page import login


class TestIntranet(unittest.TestCase):
    url = ReadYaml(location.CONFIG_FILE).yaml_data()['URL']

    def setUp(self):
        self.FF = webdriver.Chrome()
        self.FF.get(self.url)

    def testLogin(self):
        self.FF.find_element(*login.phone_number).clear()
        self.FF.find_element(*login.phone_number).send_keys('15102100358')
        self.FF.find_element(*login.password).clear()
        WebDriverWait(self.FF, 20, 0.5).until(EC.visibility_of_element_located(login.password))
        self.FF.find_element(*login.password).send_keys('123456')
        self.FF.find_element(*login.login_btn).click()
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

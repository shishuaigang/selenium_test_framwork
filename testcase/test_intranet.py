import unittest
import HTMLTestRunner

import time

import os
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from utils.readYaml import ReadYaml
from utils import location
from page import login, Menu


class TestIntranet(unittest.TestCase):
    url = ReadYaml(location.CONFIG_FILE).yaml_data()['URL']

    @classmethod
    def setUpClass(cls):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')

        cls.FF = webdriver.Chrome(executable_path="C:\Selenium\chromeDriver\chromedriver.exe", chrome_options=option)
        cls.FF.get(cls.url)
        cls.FF.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.FF.quit()

    def testLogin(self):
        self.FF.find_element(*login.phone_number).clear()
        self.FF.find_element(*login.phone_number).send_keys('15102100358')
        self.FF.find_element(*login.password).clear()
        self.FF.find_element(*login.password).send_keys('123456')
        self.FF.find_element(*login.login_btn).click()
        self.assertNotEqual(EC.visibility_of_element_located('我的工作面板'), False)

    def testSearchWorkbill(self):
        WebDriverWait(self.FF, 20, 0.5).until(EC.visibility_of_element_located(Menu.Workbill_Config))
        self.FF.find_element(*Menu.Workbill_Config).click()
        time.sleep(20)


if __name__ == '__main__':
    test_unit = unittest.TestSuite()
    now = time.strftime('%Y%m%d%H%M', time.localtime())
    print(location.REPORT_PATH)
    f = open(os.path.join(location.REPORT_PATH, 'report_' + now + '.html'), 'w', encoding='utf-8')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=u'测试报告', description='')
    test_unit.addTest(TestIntranet('testLogin'))
    test_unit.addTest(TestIntranet('testSearchWorkbill'))
    runner.run(test_unit)
    f.close()

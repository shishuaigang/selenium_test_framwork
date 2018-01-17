import HTMLTestRunner
import unittest

import os

import time
from parameterized import parameterized
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from page import login, menu
from utils import location
from utils.readYaml import ReadYaml


class TestParametrization(unittest.TestCase):
    url = ReadYaml(location.CONFIG_FILE).yaml_data()['URL']
    phonenumber = ReadYaml(os.path.join(location.DATA_PATH, 'logindata.yaml')).yaml_data()['username']
    password = ReadYaml(os.path.join(location.DATA_PATH, 'logindata.yaml')).yaml_data()['password']
    param = list(zip(phonenumber, password))

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Selenium\chromeDriver\chromedriver.exe")
        self.driver.get(self.url)
        self.driver.maximize_window()

    @parameterized.expand(param)
    def testLogin(self, username, password):
        self.driver.find_element(*login.phone_number).clear()
        self.driver.find_element(*login.phone_number).send_keys(username)
        self.driver.find_element(*login.password).clear()
        self.driver.find_element(*login.password).send_keys(password)
        self.driver.find_element(*login.login_btn).click()
        WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located(menu.MyWorkPanel))
        self.assertEqual(self.driver.find_element(*menu.MyWorkPanel).is_displayed(), True)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    test_unit = unittest.TestSuite()
    now = time.strftime('%Y%m%d%H%M', time.localtime())
    # print(location.REPORT_PATH)
    f = open(os.path.join(location.REPORT_PATH, 'report_' + now + '.html'), 'w', encoding='utf-8')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='Selenium自动化测试报告', description='')
    test_unit.addTest(unittest.makeSuite(TestParametrization))
    runner.run(test_unit)
    f.close()

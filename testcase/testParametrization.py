import unittest

import os

from parameterized import parameterized
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from drivers.driver import Driver
from commonActions.login import Login
from page import menu
from utils import location
from utils.readYaml import ReadYaml


class TestParametrization(unittest.TestCase):
    """简单的unittest参数化"""
    url = ReadYaml(location.CONFIG_FILE).yaml_data()['URL']
    phonenumber = ReadYaml(os.path.join(location.DATA_PATH, 'logindata.yaml')).yaml_data()['username']
    password = ReadYaml(os.path.join(location.DATA_PATH, 'logindata.yaml')).yaml_data()['password']
    param = list(zip(phonenumber, password))

    def setUp(self):
        self.driver = Driver().driver()
        self.driver.get(self.url)
        self.driver.maximize_window()

    @parameterized.expand(param)
    def testLogin(self, username, password):
        """参数化测试登录"""
        Login(self.driver, username, password).login()
        WebDriverWait(self.driver, 20, 0.5).until(ec.visibility_of_element_located(menu.MyWorkPanel))
        self.assertEqual(self.driver.find_element(*menu.MyWorkPanel).is_displayed(), True)

    def tearDown(self):
        self.driver.quit()

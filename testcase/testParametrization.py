import os
import unittest

from parameterized import parameterized
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from commonActions.loginsys import LoginSys
from drivers.driver import Driver
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
    @unittest.skip("测试强制跳过")
    # 装饰器调用时从下往上，执行时从上往下
    def testLogin(self, username, password):
        """参数化测试登录"""
        LoginSys(self.driver, username, password).login()
        WebDriverWait(self.driver, 20, 0.5).until(ec.visibility_of_element_located(menu.MyWorkPanel))
        self.assertEqual(self.driver.find_element(*menu.MyWorkPanel).is_displayed(), True)

    def tearDown(self):
        self.driver.quit()

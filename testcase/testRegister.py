import unittest

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from drivers.driver import Driver
from page import menu, login
from utils import location
from utils.readYaml import ReadYaml


class TestRegister(unittest.TestCase):
    """注册测试"""
    url = ReadYaml(location.CONFIG_FILE).yaml_data()['URL']

    def setUp(self):
        self.driver = Driver().driver()
        self.driver.get(self.url)
        self.driver.maximize_window()

    def testLogin(self):
        """参数化测试登录"""
        self.driver.find_element(*login.register).click()

    def tearDown(self):
        self.driver.quit()

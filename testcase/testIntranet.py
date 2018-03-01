import time
import unittest

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from commonActions.login import Login
from drivers.driver import Driver
from page import menu
from utils import location
from utils.readYaml import ReadYaml


class TestIntranet(unittest.TestCase):
    """测试内网"""
    url = ReadYaml(location.CONFIG_FILE).yaml_data()['URL']

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver().driver()
        cls.driver.get(cls.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def testLogin(self):
        """登录测试"""
        Login(self.driver, '15102100358', '123456').login()
        WebDriverWait(self.driver, 20, 0.5).until(ec.visibility_of_element_located(menu.MyWorkPanel))
        self.assertEqual(self.driver.find_element(*menu.MyWorkPanel).is_displayed(), True)

    @unittest.skip("强制跳过这个测试")
    def testSearchWorkbill(self):
        WebDriverWait(self.driver, 20, 0.5).until(ec.visibility_of_element_located(menu.Workbill_Config))
        self.driver.find_element(*menu.Workbill_Config).click()
        time.sleep(5)

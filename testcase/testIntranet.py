import time
import unittest

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from commonActions.loginsys import LoginSys
from drivers.driver import Driver
from page import menu, login
from utils import location
from utils.readYaml import ReadYaml


class TestIntranet(unittest.TestCase):
    """内网测试(串联业务,demo为登录后登出)"""
    url = ReadYaml(location.CONFIG_FILE).yaml_data()['URL']

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver().driver()
        cls.driver.get(cls.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def testLoginWithRememnerPassword(self):
        """记住密码登录测试"""
        LoginSys(self.driver, '15102100358', '123456').loginWithRememberPassword()
        WebDriverWait(self.driver, 20, 0.5).until(ec.visibility_of_element_located(menu.MyWorkPanel))
        self.assertEqual(self.driver.find_element(*menu.MyWorkPanel).is_displayed(), True)

    @unittest.skip("强制跳过普通登录测试")
    def testLogin(self):
        """普通登录测试"""
        LoginSys(self.driver, '15102100358', '123456').login()
        WebDriverWait(self.driver, 20, 0.5).until(ec.visibility_of_element_located(menu.MyWorkPanel))
        self.assertEqual(self.driver.find_element(*menu.MyWorkPanel).is_displayed(), True)

    def testLogout(self):
        """登出测试"""
        self.driver.find_element(*menu.UserInfo).click()
        time.sleep(1)
        self.driver.find_element(*menu.Logout).click()
        WebDriverWait(self.driver, 20, 0.5).until(ec.visibility_of_element_located(login.register))
        self.assertEqual(self.driver.find_element(*login.register).is_displayed(), True)

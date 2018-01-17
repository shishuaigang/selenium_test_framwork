import unittest

import time

from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from utils.readYaml import ReadYaml
from utils import location
from page import login, menu


class TestIntranet(unittest.TestCase):
    url = ReadYaml(location.CONFIG_FILE).yaml_data()['URL']

    @classmethod
    def setUpClass(cls):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')  # 隐藏'Chrome正在受到自动软件的控制'这个提示语

        cls.driver = webdriver.Chrome(executable_path=location.CHROME_DRIVER_PATH, chrome_options=option)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def testLogin(self):
        self.driver.find_element(*login.phone_number).clear()
        self.driver.find_element(*login.phone_number).send_keys('15102100358')
        self.driver.find_element(*login.password).clear()
        self.driver.find_element(*login.password).send_keys('123456')
        self.driver.find_element(*login.login_btn).click()
        WebDriverWait(self.driver, 20, 0.5).until(ec.visibility_of_element_located(menu.MyWorkPanel))
        self.assertEqual(self.driver.find_element(*menu.MyWorkPanel).is_displayed(), True)

    def testSearchWorkbill(self):
        WebDriverWait(self.driver, 20, 0.5).until(ec.visibility_of_element_located(menu.Workbill_Config))
        self.driver.find_element(*menu.Workbill_Config).click()
        time.sleep(20)

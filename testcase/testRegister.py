import unittest

import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from drivers.driver import Driver
from page import menu, login, register
from utils import location
from utils import getMobileCode, createPhonenumber
from utils.readYaml import ReadYaml


class TestRegister(unittest.TestCase):
    """注册测试"""
    url = ReadYaml(location.CONFIG_FILE).yaml_data()['URL']
    randomPhoneNumber = createPhonenumber.createRandomPhoneNumber()

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver().driver()
        cls.driver.get(cls.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def testRegister_1(self):
        """注册第一步"""
        cookie = {self.driver.get_cookies()[0]['name']: self.driver.get_cookies()[0]['value']}
        self.driver.find_element(*login.register).click()
        self.driver.find_element(*register.inputPhonenumber).send_keys(self.randomPhoneNumber)
        mobcode = getMobileCode.getmobilecode(self.url, self.randomPhoneNumber, cookie)
        self.driver.find_element(*register.mobileCode).send_keys(mobcode)
        time.sleep(5)
        self.driver.find_element(*register.nextStep).click()
        WebDriverWait(self.driver, 20, 0.5).until(ec.visibility_of_element_located(register.male))
        self.assertEqual(self.driver.find_element(*register.male).is_displayed(), True)
        self.assertEqual(self.driver.find_element(*register.female).is_displayed(), True)

    def testRegister_2(self):
        """注册第二步"""
        self.driver.find_element(*register.inputName).send_keys('测试' + self.randomPhoneNumber)
        self.driver.find_element(*register.female).click()
        self.driver.find_elements(*register.inputPassword)[1].send_keys('123456')  # 这里有点问题，根据属性值定位不到
        self.driver.find_element(*register.confirmPassword).send_keys('123456')
        self.driver.find_element(*register.chooseDep).click()
        self.driver.find_element(*register.chooseInroadChemicalPlant).click()
        self.driver.find_element(*register.registerBtn).click()
        WebDriverWait(self.driver, 20, 0.5).until(ec.visibility_of_element_located(login.register))
        self.assertEqual(self.driver.find_element(*login.register).is_displayed(), True)

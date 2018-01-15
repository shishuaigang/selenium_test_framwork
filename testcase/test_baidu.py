import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.readYaml import ReadYaml
from utils import location


class TestBaidu(unittest.TestCase):
    url = ReadYaml(location.CONFIG_FILE).yaml_data()['URL']
    phone_number = (By.XPATH, '//*[@id="login-form"]/fieldset/label[1]/span/input')
    password = (By.XPATH, '//*[@id="login-form"]/fieldset/label[2]/span/input')

    def setUp(self):
        self.FF = webdriver.Chrome()
        self.FF.get(self.url)

    def testSearch(self):
        self.FF.find_element(*self.phone_number).clear()
        self.FF.find_element(*self.phone_number).send_keys('15102100358')
        time.sleep(5)

    def tearDown(self):
        self.FF.quit()


if __name__ == '__main__':
    unittest.main()

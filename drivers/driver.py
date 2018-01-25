from selenium import webdriver

from utils import location
from utils.readYaml import ReadYaml


class Driver:
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')  # 隐藏'Chrome正在受到自动软件的控制'这个提示语

        browser_info = ReadYaml(location.CONFIG_FILE).yaml_data()

        if browser_info['Browser'].upper() == 'CHROME':
            print("Please confirm the matching releationship of chromedriver and chrome")
            self.d = webdriver.Chrome(executable_path=browser_info['BROWSER_DRIVER_PATH'], chrome_options=option)

        elif browser_info['Browser'].upper() == 'FIREFOX':
            print("Please confirm the matching releationship of geckodriver and firefox")
            self.d = webdriver.Firefox(executable_path=browser_info['BROWSER_DRIVER_PATH'])

        else:
            print("Please use chrome or firefox, thanks!")
            self.d = None

    def driver(self):
        return self.d

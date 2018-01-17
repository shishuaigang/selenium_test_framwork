"""
以此文件为基准，去定位其他文件的位置
os.path.join通用于windows和linux，多采用此方法去拼接文件夹

"""

import os

#  BasePath = os.path.abspath(__file__)  # 当前文件的绝对路径
# CurrentDir = os.path.dirname(os.path.abspath(__file__))  # 当前文件的目录
ROOT_DIR = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

CONFIG_PATH = os.path.join(ROOT_DIR, 'config')
CONFIG_FILE = os.path.join(ROOT_DIR, 'config', 'config.yaml')
DATA_PATH = os.path.join(ROOT_DIR, 'data')
DRIVER_PATH = os.path.join(ROOT_DIR, 'drivers')
LOG_PATH = os.path.join(ROOT_DIR, 'page')
REPORT_PATH = os.path.join(ROOT_DIR, 'report')
TESTCASE_PATH = os.path.join(ROOT_DIR, 'testcase')
UTILS_PATH = os.path.join(ROOT_DIR, 'utils')

CHROME_DRIVER_PATH = r"C:\Selenium\chromeDriver\chromedriver.exe"
FIREFOX_DRIVER_PATH = r"C:\Selenium\firefoxDriver\geckodriver.exe"

import HTMLTestRunner
import unittest

import time
import sys
import os
from testcase.testIntranet import TestIntranet
from testcase.testParametrization import TestParametrization
from utils import location, getTime
from utils.sendMail import SendMail


@getTime.gettime
def main():
    sys.path.append(location.ROOT_DIR)  # 将整个项目文件夹加入环境变量,这样不会出现在cmd运行中no import moudle的问题
    test_unit = unittest.TestSuite()
    now = time.strftime('%Y%m%d%H%M', time.localtime())
    # print(location.REPORT_PATH)
    f = open(os.path.join(location.REPORT_PATH, 'report_' + now + '.html'), 'w', encoding='utf-8')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='Selenium自动化测试报告', description='')
    test_unit.addTest(TestIntranet('testLogin'))
    test_unit.addTest(TestIntranet('testSearchWorkbill'))
    test_unit.addTest(unittest.makeSuite(TestParametrization))
    runner.run(test_unit)
    f.close()
    SendMail(now).send_mail()


if __name__ == '__main__':
    main()

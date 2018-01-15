from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib

import os

from utils.readYaml import ReadYaml
from utils import location


class SendMail:
    def __init__(self, timestamp):
        self.tsmp = timestamp

    def send_mail(self):
        # 定义发件人邮箱，密码和收件人的list
        sender = ReadYaml(location.CONFIG_FILE).yaml_data()['mail_sender']
        passwd = ReadYaml(location.CONFIG_FILE).yaml_data()['mail_password']
        receiver = ReadYaml(location.CONFIG_FILE).yaml_data()['mail_recivers']
        msg = MIMEMultipart()
        msg["Subject"] = 'Selenium自动化测试报告'  # 邮件主题
        msg["From"] = sender
        msg["To"] = ','.join(receiver)  # 收件人邮箱列表，以逗号分隔
        #  邮件正文
        part_con = MIMEText(
            "Hi all,\nThis is Selenium自动化测试报告 ", 'plain', 'utf-8')
        msg.attach(part_con)  # 邮件添加正文
        report_file_path = os.path.join(location.REPORT_PATH, 'report_' + self.tsmp + '.html')
        if os.path.exists(report_file_path):
            part_attach = MIMEApplication(open(report_file_path, 'rb').read())
            part_attach.add_header('Content-Disposition', 'attachment', filename='report_' + self.tsmp + '.html')
            msg.attach(part_attach)  # 邮件添加附件
            s = smtplib.SMTP("smtp.exmail.qq.com", timeout=30)  # 连接邮件服务器
            s.login(sender, passwd)  # 登录服务器
            s.sendmail(sender, receiver, msg.as_string())  # 发送邮件
            print("邮件发送成功")
            s.close()
        else:
            raise FileNotFoundError("测试报告不存在")


if __name__ == '__main__':
    SendMail('201801151620').send_mail()

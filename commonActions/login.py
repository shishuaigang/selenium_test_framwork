from page import login


class Login:
    def __init__(self, driver, username, password):
        self.uname = username
        self.pwd = password
        self.d = driver

    def login(self):
        self.d.find_element(*login.phone_number).clear()
        self.d.find_element(*login.phone_number).send_keys(self.uname)
        self.d.find_element(*login.password).clear()
        self.d.find_element(*login.password).send_keys(self.pwd)
        self.d.find_element(*login.login_btn).click()

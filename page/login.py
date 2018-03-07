from selenium.webdriver.common.by import By

phone_number = (By.CSS_SELECTOR, 'input[name=phonenumber]')
password = (By.CSS_SELECTOR, 'input[name=password]')
login_btn = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-block.btn-primary')
remember_password = (By.CSS_SELECTOR, 'span.lbl')
register = (By.LINK_TEXT, '立即注册')
forget_password = (By.LINK_TEXT, '忘记密码')

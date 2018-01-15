from selenium.webdriver.common.by import By

phone_number = (By.XPATH, '//*[@id="login-form"]/fieldset/label[1]/span/input')
password = (By.XPATH, '//*[@id="login-form"]/fieldset/label[2]/span/input')
login_btn = (By.XPATH, '//*[@id="login-form"]/fieldset/button')
remember_password = (By.XPATH, '//*[@id="login-form"]/fieldset/div[1]/label/span')
register = (By.XPATH, '//*[@id="login-form"]/fieldset/div[3]/a[1]')
forget_password = (By.XPATH, '//*[@id="login-form"]/fieldset/div[3]/a[2]')

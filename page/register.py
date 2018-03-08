from selenium.webdriver.common.by import By

backtoLoginPage = (By.LINK_TEXT, '返回登录')
inputPhonenumber = (By.CSS_SELECTOR, 'input[name=phonenumber][placeholder=请输入您的手机号]')
mobileCode = (By.CSS_SELECTOR, '#signup-mob-form > fieldset > label:nth-child(2) > div > input')
getMobileCode = (By.CSS_SELECTOR, 'button.btn.btn-success.js-getMobCode')
nextStep = (By.CSS_SELECTOR, '#signup-mob-form > fieldset > button')

inputName = (By.CSS_SELECTOR, 'input[name=username]')
male = (By.CSS_SELECTOR, 'input[name=sex][value=男]')
female = (By.CSS_SELECTOR, 'input[name=sex][value=女]')
inputPassword = (By.CSS_SELECTOR, 'input[name="password"][placeholder="6-20个字符(区分大小写)"]')
confirmPassword = (By.CSS_SELECTOR, 'input[name=confirmpassword]')

chooseDep = (By.CSS_SELECTOR, '#tree-deptlist > button')
chooseInroadChemicalPlant = (
    By.CSS_SELECTOR, '#tree-deptlist > ul > li > div.scroll-content > div > ul > li:nth-child(2) > div')
registerBtn = (By.CSS_SELECTOR, '#signup-info-form > fieldset > div.row > div:nth-child(2) > button')
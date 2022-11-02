from selenium.webdriver.common.by import By
import time
from utilities.customLogger import LogGen

class LoginPage():
    
    lg = LogGen.loggen()  # logging
    
    #locators
    _email_login_id = 'input-email'
    _passoword_login_id ='input-password'
    _button_login_xpath = '//input[@value="Zaloguj"]'
    _msg_my_account_xpath = '//h2[text()="Moje konto"]'
    
    def __init__(self, driver):
        self.driver = driver 
    
    def setMailLogin(self, mail):
        sendMailLogin = self.driver.find_element(By.ID, self._email_login_id)
        sendMailLogin.clear()
        sendMailLogin.send_keys(mail)
    
    def setPasswordLogin(self, password):
        sendPasswordLogin = self.driver.find_element(By.ID, self._passoword_login_id)
        sendPasswordLogin.clear()
        sendPasswordLogin.send_keys(password)
    
    def clickbuttonLogin(self):
        button = self.driver.find_element(By.XPATH, self._button_login_xpath)
        button.click()
    
    def login(self, mail, password):
        
        time.sleep(2)
        self.setMailLogin(mail)
        time.sleep(2)
        self.setPasswordLogin(password)
        time.sleep(2)
        self.clickbuttonLogin()        
        
    def isMyAccountPage(self):
        try:
            return self.driver.find_element(By.XPATH, self._msg_my_account_xpath).is_displayed()
        except:
            return False
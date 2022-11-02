from selenium.webdriver.common.by import By

class HomePage():

    #locators
    _my_account_xpath = '//span[text()="Moje konto"]'
    _register_xpath = '//a[text()="Rejestracja"]'
    _login_xpath = '//a[text()="Logowanie"]'
    
    def __init__(self, driver):
        self.driver = driver
    
    def clickMyAccount(self):
        link_my_account = self.driver.find_element(By.XPATH, self._my_account_xpath)        
        link_my_account.click()
        
    def clickRegister(self):
        link_register = self.driver.find_element(By.XPATH, self._register_xpath)
        link_register.click()
    
    def clikLogin(self):
        link_login = self.driver.find_element(By.XPATH, self._login_xpath)
        link_login.click()                
    
      
from selenium.webdriver.common.by import By

class MyAccountPage():

    #locators
    _link_logout_xpath = '//div[@class="list-group"]//a[text()="Wyloguj"]'
    _button_accept_xpath = '//a[text()="Zatwierdź"]'
    
    def __init__(self, driver):
        self.driver = driver
    
    def clickLogout(self):
        link_logout = self.driver.find_element(By.XPATH, self._link_logout_xpath)        
        link_logout.click()
    
    def clickAccept(self):
        button_accept = self.driver.find_element(By.XPATH, self._button_accept_xpath)        
        button_accept.click()    
    
    def logout(self):
        self.clickLogout()
        self.clickAccept()
        
            
     
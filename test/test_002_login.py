import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from utilities.random_string import *
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestTCLF002:
    
    lg = LogGen.loggen()
    lg.info('*** Lauching page class TestTCLF002 ***')
    
    rc = ReadConfig()
    baseUrl = rc.getApplicationURL()
    #username = rc.getUseremail()
    #password = rc.getPassword()
    
    username = 'xyzabc123@gmail.com'
    password = '12345'
    
    @pytest.mark.log
    def test_account_login(self, setup):
        
        self.lg.info('*** TC_LF_002_account_login --> START ***')
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        
        self.hp.clickMyAccount()
        self.lg.info('*** Clicking MyAccount --> Login ***')
        self.hp.clikLogin()
        self.lg.info('*** Clicking Login ***')
      
        self.lg.info('*** Loging ***')   
        self.lp.login(self.username, self.password)
                
        msg2 = self.lp.isAlertLogin()
        self.lg.info('*** TC_LF_002_alert_login --> END ***')
        
        if msg2 == True:
            self.lg.info('Assert is OK')
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+'\\Project OpenCartDemo\\screenshots\\alert_login.png')
            self.lg.info("Assert False")
            self.driver.close()
            assert False
          
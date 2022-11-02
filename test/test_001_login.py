import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from utilities.random_string import *
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestTCLF001:
    
    lg = LogGen.loggen()
    
    lg.info('*** Lauching page class TestTCLF001 ***')
    
    rc = ReadConfig()
    baseUrl = rc.getApplicationURL()
    username = rc.getUseremail()
    password = rc.getPassword()
 
    @pytest.mark.log
    def test_account_login(self, setup):
        
        self.lg.info('*** TC_LF_001_account_login --> START ***')
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
                
        msg2 = self.lp.isMyAccountPage()
        self.lg.info('*** TC_LF_001_account_login --> END ***')
        
        if msg2 == True:
            self.lg.info('Assert is OK')
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot('H:\\Klon\\Project OpenCartDemo\\screenshots\\test_account_reg.png')
            self.lg.info("Assert False")
            self.driver.close()
            assert False
          
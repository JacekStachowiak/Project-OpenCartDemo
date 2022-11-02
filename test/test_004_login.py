import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from utilities.random_string import *
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time

class TestTC_LF_006:
    
    lg = LogGen.loggen()
    lg.info('*** Lauching page class TC_LF_006 ***')
    
    rc = ReadConfig()
    baseUrl = rc.getApplicationURL()

    @pytest.mark.log
    def test_forgotten_password(self, setup):
        
        self.lg.info('*** TC_LF_006_account_login --> START ***')
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        
        self.hp.clickMyAccount()
        self.lg.info('*** Clicking MyAccount --> Login ***')
        self.hp.clikLogin()
        self.lg.info('*** Clicking Login ***')
        self.lg.info('*** Loging ***')   
        
        forg = self.lp.isForgottenPassword()
        self.lg.info('*** TC_LF_006_forg --> END ***')

        if forg == 'Zapomniałem hasła':
            self.lg.info('Assert is OK')
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+'\\Project OpenCartDemo\\screenshots\\forg.png')
            self.lg.info("Assert False")
            self.driver.close()
            assert False
        
        time.sleep(3)
        
        self.lp.clickforgottenPassword()
        self.lg.info('*** TC_LF_006_click forgoten password ***')
        
        forg_page = self.lp.isForgottenPasswordPage()
        self.lg.info('*** TC_LF_006_forg_page --> END ***')
                
        if forg_page == 'Zapomniałeś hasła?':
            self.lg.info('Assert is OK')
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+'\\Project OpenCartDemo\\screenshots\\forg_page.png')
            self.lg.info("Assert False")
            self.driver.close()
            assert False            
          
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.my_account_page import MyAccountPage
from selenium.webdriver.common.by import By
from utilities.random_string import *
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time
import pytest


class Test_003_Login_ddt:
    
    lg = LogGen.loggen()
    
    lg.info('*** Lauching page test_003 ***')
    
    rc = ReadConfig()
    baseUrl = rc.getApplicationURL()
    #path = 'H:\\Klon\\Project OpenCartDemo\\test\\test data\\Opencart_LoginData.xlsx'
    path = os.path.abspath(os.curdir)+'\\testdata\\Opencart_LoginData.xlsx'
    
    @pytest.mark.login
    def test_login_ddt(self, setup):
        
        self.lg.info('*** Test_003_account_login_ddt --> START ***')
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []
        
        self.driver = setup
        self.driver.get(self.baseUrl)
        
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ap = MyAccountPage(self.driver)
        
        for r in range(2, self.rows+1):
            self.hp.clickMyAccount()
            self.lg.info('*** Clicking MyAccount --> Login test_003***')
            self.hp.clikLogin()
            self.lg.info('*** Clicking Login test_003***')
            
            self.lg.info('*** Loging  test_003 ***')
            self.mail = XLUtils.readData(self.path, 'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1',r,2)
            self.exp = XLUtils.readData(self.path, 'Sheet1',r,3)
            
            self.lp.login(self.mail, self.password)
            time.sleep(4)
            msg2 = self.lp.isMyAccountPage()
            self.lg.info('*** test_003_account_login --> END ***')
            
            if self.exp == 'Valid':
                if msg2 == True:
                    lst_status.append('Pass')
                    self.ap.logout()
                else:
                    lst_status.append('Fail')
            
            elif self.exp == 'Invalid':
                if msg2 == True:
                    lst_status.append('Fail')
                    self.lp.login()
                else:
                    lst_status.append('Pass')
        self.driver.close()                    
        
        if 'Fail' is not lst_status:
            assert True
        else:
            assert False
        self.lg.info('********** End test_003_login_ddt ************* ')        
            
        
        
        
        
        


from pages.register_page import RegisterPage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from utilities.random_string import *
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest


class Test_001_AccountReg:
    
    lg = LogGen.loggen()
    
    baseURL = ReadConfig.getApplicationURL()
    lg.info('*** Lauching page ***') 
    
    @pytest.mark.regression
    def test_account_reg(self, setup):
        
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.rp = RegisterPage(self.driver)
                
        self.hp.clickMyAccount()
        self.lg.info('*** Clicking MyAccount --> Register ***') 
        self.hp.clickRegister()
        self.lg.info('*** Clicking Register ***') 
        
        firstname = random_first_name()
        lastname = random_last_name()
        email = random_mail()
        number_phone = '456 567 678'
        adress = 'Krzakowa 34'
        city = 'Warsaw'
        postcode = '00-950'
        pwd = random_password()
        confirm_pwd = pwd
        
        self.lg.info('*** test_001_account_registration --> START ***')                
        self.rp.register(firstname, lastname, email, number_phone, adress, city, postcode)
        self.lg.info('*** Register section finished ***')
        self.rp.password(pwd, confirm_pwd)
        self.lg.info('*** Password section finished ***')
        self.rp.checkbox()
        self.lg.info('*** Checkbox section finished ***')
        self.rp.button()
        
        msg_1 = self.rp.msgCreateAccount()
                       
        if msg_1 == 'Twoje konto zostało stworzone!':
            self.lg.info('Assert is passed')
            assert True
            self.driver.close()
        else:
            #self.driver.save_screenshot(os.getcwd()+"\\screenshots\\test_account_reg.png")  # nazwa pliku --> nazwa methody
            self.driver.save_screenshot('H:\\Klon\\Project OpenCartDemo\\screenshots\\test_account_reg.png')  # nazwa pliku --> nazwa methody
            self.lg.info('Assert is False')
            self.driver.close()
            assert False
        self.lg.info('*** test_001_account_registration --> END ***')    
        
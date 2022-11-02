from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
import time
from selenium.webdriver.support.select import Select
from utilities.customLogger import LogGen


class RegisterPage():
    
    lg = LogGen.loggen()  # logging
    
    #locators
    _first_name_id = 'input-firstname'
    _last_name_id = 'input-lastname'
    _email_id = 'input-email'
    _phone_id = 'input-telephone'
    _adress1_id = 'input-address-1'
    _city_id = 'input-city'
    _post_code_id = 'input-postcode'
    _country_select = 'input-country'
    _zone_select_id = 'input-zone'
    _password_id = 'input-password'
    _confirm_password_id = 'input-confirm'
    _subscribe_xpath = '//input[@name="newsletter" and @value="1"]'
    _privacy_policy_xpath = '//input[@name="agree"]'
    _button_xpath = '//input[@class="btn btn-primary"]'
    _create_msg_xpath = '//h1[text()="Twoje konto zostało stworzone!"]'
    
    def __init__(self, driver):
        self.driver = driver 
    
    def setFirstName(self, firstname):
        sendFirstName = self.driver.find_element(By.ID, self._first_name_id)
        sendFirstName.clear()
        sendFirstName.send_keys(firstname)
    
    def setLastName(self, lastname):
        sendLastName = self.driver.find_element(By.ID, self._last_name_id)
        sendLastName.clear()
        sendLastName.send_keys(lastname)
    
    def setEmail(self, email):
        sendEmail = self.driver.find_element(By.ID, self._email_id)
        sendEmail.clear()
        sendEmail.send_keys(email)

    def setPhone(self, number_phone):
        sendPhone = self.driver.find_element(By.ID, self._phone_id)
        sendPhone.clear()
        sendPhone.send_keys(number_phone)   
    
    def setAdress1(self, adress):
        sendPhone = self.driver.find_element(By.ID, self._adress1_id)
        sendPhone.clear()
        sendPhone.send_keys(adress)     
    
    def setCity(self, city):
        sendCity = self.driver.find_element(By.ID, self._city_id)
        sendCity.clear()
        sendCity.send_keys(city)                         
    
    def setPostCode(self, postcode):
        sendPostcode = self.driver.find_element(By.ID, self._post_code_id)
        sendPostcode.clear()
        sendPostcode.send_keys(postcode)
    
    def selectCountry(self):
        selectCountry = self.driver.find_element(By.ID, self._country_select)
        country = Select(selectCountry)
        country.select_by_visible_text('Poland')   
    
    def selectZone(self):
        selectZone = self.driver.find_element(By.ID, self._zone_select_id)
        zone = Select(selectZone)
        zone.select_by_visible_text('Lubuskie')              
    
    def setPassword(self, pwd):
        sendPassword = self.driver.find_element(By.ID, self._password_id)
        sendPassword.clear()
        sendPassword.send_keys(pwd)
    
    def setConfirmPassword(self, confirm_pwd):
        sendPassword = self.driver.find_element(By.ID, self._confirm_password_id)
        sendPassword.clear()
        sendPassword.send_keys(confirm_pwd)
    
    def setSubscribe(self):
        clickSubscribe = self.driver.find_element(By.XPATH, self._subscribe_xpath)
        clickSubscribe.click()
    
    def setPrivacyPolicy(self):
        checkPrivacyPolicy = self.driver.find_element(By.XPATH, self._privacy_policy_xpath)
        checkPrivacyPolicy.click()
            
    def clickbuttonContinue(self):
        mywait = WebDriverWait(self.driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                      ElementNotVisibleException,
                                                                                      ElementNotSelectableException,
                                                                                      Exception])
        button = mywait.until(EC.element_to_be_clickable((By.XPATH, self._button_xpath)))
        #button = self.driver.find_element(By.XPATH, self._button_xpath)
        button.click()
    
        
    def register(self, firstname, lastname, email, number_phone, adress, city, postcode):
        
        self.setFirstName(firstname)
        time.sleep(1)
        self.setLastName(lastname)
        time.sleep(1)
        self.setEmail(email)
        time.sleep(1)
        self.setPhone(number_phone)
        time.sleep(1)
        self.setAdress1(adress)
        time.sleep(1)
        self.setCity(city)
        time.sleep(1)
        self.setPostCode(postcode)
        time.sleep(1)
        self.selectCountry()
        time.sleep(1)
        self.selectZone()
        time.sleep(1)
        
            
    def password(self,pwd, confirm_pwd):
        self.setPassword(pwd)
        time.sleep(1)
        self.setConfirmPassword(confirm_pwd)
        time.sleep(1)
        
                
    def checkbox(self):
        self.setSubscribe()
        time.sleep(2)
        self.setPrivacyPolicy()
        time.sleep(2)       
    
    def button(self):
        self.clickbuttonContinue()
        time.sleep(5)
        
                
    def msgCreateAccount(self):
        try:
            result = self.driver.find_element(By.XPATH, self._create_msg_xpath).text
            return result
        except:
            None            

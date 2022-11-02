from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, Exception 

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-notifications') 
#options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.implicitly_wait(10)
baseUrl = 'https://demo.opencart.com/index.php?route=account/register&language=en-gb'
driver.get(baseUrl)
mywait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                ElementNotVisibleException,
                                                                                ElementNotSelectableException,
                                                                                Exception])

_first_name_id = 'input-firstname'
_last_name_id = 'input-lastname'
_email_id = 'input-email'
_password_id = 'input-password'
_subscribe_xpath = '//input[@id="input-newsletter-yes"]'
_privacy_policy_xpath = '//input[@class="form-check-input"][@name="agree"]'
_button_xpath = '//button[normalize-space()="Continue"]'
_create_msg_xpath = '//*[@id="content"]/h1'


sendFirstName = driver.find_element(By.ID, _first_name_id)
sendFirstName.clear()
sendFirstName.send_keys('jack4567')
time.sleep(3)
sendLastName = driver.find_element(By.ID, _last_name_id)
sendLastName.clear()
sendLastName.send_keys('stachkowalski')
time.sleep(3)
sendEmail = driver.find_element(By.ID, _email_id)
sendEmail.clear()
sendEmail.send_keys('4811176@gmail.com')
time.sleep(3)
sendPassword = driver.find_element(By.ID, _password_id)
sendPassword.clear()
sendPassword.send_keys('jsj123873')
time.sleep(3)
clickSubscribe = driver.find_element(By.XPATH, _subscribe_xpath)
clickSubscribe.click()
time.sleep(3)    
checkPrivacyPolicy = driver.find_element(By.XPATH, _privacy_policy_xpath)
checkPrivacyPolicy.click()
time.sleep(3)
button = mywait.until(EC.element_to_be_clickable((By.XPATH, _button_xpath))) # czekaj do póki się nie pojawi
button.click()

msg = driver.find_element(By.XPATH, _create_msg_xpath).text
print(msg)

time.sleep(6)
driver.quit()
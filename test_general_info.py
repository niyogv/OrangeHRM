import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

# login details
URL='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
USER='Admin'
PASSWORD='admin123'

# General information
ORGNAME='sarvalabs'
REGNUMBER='123456'
TAXID='1234'
PHONE='9999999999'
FAX='1234'

class Test_orangeDashboard():

    @pytest.fixture
    def test_invoke(self):
        self.driver=webdriver.Chrome()
        wait=WebDriverWait(self.driver, 60)
        self.driver.get(URL)
        username=wait.until(Ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))
        username.send_keys(USER)
        password=wait.until(Ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
        password.send_keys(PASSWORD)
        self.driver.find_element(By.TAG_NAME, 'button').click()
        h6TitleCheck=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'h6')))
        assert h6TitleCheck.text=='Dashboard'

    def test_pay_grades(self,test_invoke):
        wait=WebDriverWait(self.driver, 60)
        self.driver.find_element(By.XPATH, '//ul[@class="oxd-main-menu"]/li[1]').click()
        h6TitleCheck=wait.until(Ec.presence_of_element_located((By.XPATH, '//span[@class="oxd-topbar-header-breadcrumb"]/h6')))
        assert h6TitleCheck.text=="Admin"
        self.driver.find_element(By.XPATH, '//div[@class="oxd-topbar-body"]/nav/ul/li[3]').click()
        info=wait.until(Ec.presence_of_element_located((By.LINK_TEXT, 'General Information')))
        ActionChains(self.driver).move_to_element(info).click().perform()
        h6TitleCheck1=wait.until(Ec.presence_of_element_located((By.XPATH, '//div[@class="orangehrm-header-container"]/h6')))
        assert h6TitleCheck1.text=='General Information'
        self.driver.find_element(By.XPATH, '//div[@class="orangehrm-header-container"]/div/label/span').click()
        orgname=wait.until(Ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input')))
        orglength=len(orgname.get_attribute('value'))
        for i in range(orglength):
            orgname.send_keys(Keys.BACKSPACE)
        orgname.send_keys(ORGNAME)
        regnumber=wait.until(Ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input')))
        regnumlength=len(regnumber.get_attribute('value'))
        for i in range(regnumlength):
            regnumber.send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys(REGNUMBER)
        taxid=self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input')
        taxidlength=len(taxid.get_attribute('value'))
        for i in range(taxidlength):
            taxid.send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys(TAXID)
        phone=self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input')
        phonelength=len(phone.get_attribute('value'))
        for i in range(phonelength):
            phone.send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input').send_keys(PHONE)
        fax=self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/input')
        faxlength=len(fax.get_attribute('value'))
        for i in range(faxlength):
            fax.send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/input').send_keys(FAX)
        self.driver.find_element(By.XPATH, '//div[@class="oxd-form-actions"]/button').click()
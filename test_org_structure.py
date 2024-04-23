import random
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


# Base url
URL='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

# Login cred
USERNAME='Admin'
PASSWORD='admin123'

# Location details
UNIT=''.join(random.choices(string.digits, k=4))
ADMIN=''.join(random.choices(string.ascii_letters, k=6))
ORG=''.join(random.choices(string.ascii_letters, k=4))

class Test_ore_structure():

    @pytest.fixture
    def test_invoke(self):
        self.driver=webdriver.Chrome()
        self.driver.get(URL)
        wait=WebDriverWait(self.driver, 60)
        username=wait.until(Ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))
        username.send_keys(USERNAME)
        password=wait.until(Ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
        password.send_keys(PASSWORD)
        button=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'button')))
        button.click()
        h6TitleCheck=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'h6')))
        assert h6TitleCheck.text=='Dashboard'
        self.driver.find_element(By.XPATH, '//ul[@class="oxd-main-menu"]/li[1]').click()
        h6TitleCheck1=wait.until(Ec.presence_of_element_located((By.XPATH, '//span[@class="oxd-topbar-header-breadcrumb"]/h6')))
        assert h6TitleCheck1.text=="Admin"
        self.driver.find_element(By.XPATH, '//div[@class="oxd-topbar-body"]/nav/ul/li[3]').click()
        structure=wait.until(Ec.element_to_be_clickable((By.LINK_TEXT, 'Structure')))
        structure.click()
        h6TitleCheck2=wait.until(Ec.presence_of_element_located((By.XPATH, '//div[@class="orangehrm-header-container"]/h6')))
        assert h6TitleCheck2.text=='Organization Structure', 'failed to fetch org form'
        edit=wait.until(Ec.element_to_be_clickable((By.XPATH, '//div[@class="orangehrm-header-container"]/div/label/span')))
        edit.click()

    def test_edit_org_structure(self,test_invoke):
        wait=WebDriverWait(self.driver, '60')
        self.driver.find_element(By.XPATH, '//div[@class="oxd-sheet oxd-sheet--rounded oxd-sheet--gutters oxd-sheet--pastel-white org-structure-card --edit"]/div[2]/button[2]').click()
        unitid=wait.until(Ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/form/div[1]/div/div[2]/input')))
        unitidlenngth=len(unitid.get_attribute('value'))
        for i in range(unitidlenngth):
            unitid.send_keys(Keys.BACKSPACE)
        unitid.send_keys(UNIT)
        admin=self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/form/div[2]/div/div[2]/input')
        adminlenght=len(admin.get_attribute('value'))
        for i in range(adminlenght):
            admin.send_keys(Keys.BACKSPACE)
        admin.send_keys(ADMIN)
        self.driver.find_element(By.XPATH, '//div[@class="oxd-form-actions"]/button[2]').click()

    def test_add_org_structure(self,test_invoke):
        wait=WebDriverWait(self.driver, 60)
        addbutton=wait.until(Ec.presence_of_element_located((By.XPATH, '//div[@class="org-root-container"]/button')))
        addbutton.click()
        time.sleep(4)
        unitid=wait.until(Ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/form/div[1]/div/div[2]/input')))
        unitidlenngth=len(unitid.get_attribute('value'))
        for i in range(unitidlenngth):
            unitid.send_keys(Keys.BACKSPACE)
        unitid.send_keys(UNIT)
        admin=self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/form/div[2]/div/div[2]/input')
        adminlenght=len(admin.get_attribute('value'))
        for i in range(adminlenght):
            admin.send_keys(Keys.BACKSPACE)
        admin.send_keys(ORG)
        self.driver.find_element(By.XPATH, '//div[@class="oxd-form-actions"]/button[2]').click()
        time.sleep(4)


import random
import string
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.action_chains import ActionChains

URL='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
USER='Admin'
PASSWORD='admin123'

# Shift details
NAME=''.join(random.choices(string.ascii_letters, k=4))
FROM='09:00 AM'
ASSIGNED=''.join(random.choices(string.ascii_letters, k=4))

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
        self.driver.find_element(By.XPATH, '//div[@class="oxd-topbar-body"]/nav/ul/li[2]').click()
        paygrades=wait.until(Ec.presence_of_element_located((By.LINK_TEXT, 'Work Shifts')))
        ActionChains(self.driver).move_to_element(paygrades).click().perform()
        h6TitleCheck1=wait.until(Ec.presence_of_element_located((By.XPATH, '//div[@class="orangehrm-header-container"]/h6')))
        assert h6TitleCheck1.text=='Work Shifts'
        self.driver.find_element(By.XPATH, '//div[@class="orangehrm-header-container"]/div/button').click()
        h6TitleCheck2=wait.until(Ec.presence_of_element_located((By.XPATH, '//div[@class="orangehrm-card-container"]/h6')))
        assert h6TitleCheck2.text=="Add Work Shift"
        name=wait.until(Ec.presence_of_element_located((By.XPATH, '//div[@class="oxd-input-group oxd-input-field-bottom-space"]/div[2]/input')))
        name.send_keys(NAME)
        self.driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-clock oxd-time-input--clock"]').click()
        fromhour=self.driver.find_element(By.XPATH, '//div[@class="oxd-time-hour-input"]/i')
        ActionChains(self.driver).move_to_element(fromhour).double_click().perform()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/div[1]/label').click()
        self.driver.find_element(By.XPATH, '//input[@placeholder="Type for hints..."]').send_keys(ASSIGNED)
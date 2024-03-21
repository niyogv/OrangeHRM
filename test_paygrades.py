import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import pytest

URL='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
USER='Admin'
PASSWORD='admin123'

# Scenario : login click on admin select job dropdown selects paygrades add's user and select the currency type enters min and max salary click on save

# Paygrades details
NAME=''.join(random.choices(string.ascii_letters,k=4))
MIN=''.join(random.choices(string.digits, k=4))
MAX=''.join(random.choices(string.digits, k=6))

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
        paygrades=wait.until(Ec.presence_of_element_located((By.LINK_TEXT, 'Pay Grades')))
        ActionChains(self.driver).move_to_element(paygrades).click().perform()
        h6TitleCheck1=wait.until(Ec.presence_of_element_located((By.XPATH, '//div[@class="orangehrm-header-container"]/h6')))
        assert h6TitleCheck1.text=='Pay Grades'
        self.driver.find_element(By.XPATH, '//div[@class="orangehrm-header-container"]/div/button').click()
        h6TitleCheck2=wait.until(Ec.presence_of_element_located((By.XPATH, '//div[@class="orangehrm-card-container"]/h6')))
        assert h6TitleCheck2.text=='Add Pay Grade'
        self.driver.find_element(By.XPATH, '//div[@class="oxd-input-group oxd-input-field-bottom-space"]/div[2]/input').send_keys(NAME)
        self.driver.find_element(By.XPATH, '//div[@class="oxd-form-actions"]/button[2]').click()
        wait.until(Ec.element_to_be_clickable((By.XPATH, '//div[@class="orangehrm-header-container"]/div/button'))).click()
        wait.until(Ec.element_to_be_clickable((By.XPATH, '//div[@class="oxd-select-text oxd-select-text--active"]/div[2]'))).click()
        currency=wait.until(Ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/div/div/div[2]/div/div[2]')))
        ActionChains(self.driver).move_to_element(currency).click().perform()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[1]/div/div[2]/input').send_keys(MIN)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/div/div[2]/input').send_keys(MAX)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/form/div[3]/button[2]').click()

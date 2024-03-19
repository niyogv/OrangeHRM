import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec

URL='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
USER='Admin'
PASSWORD='admin123'

# Scenario : login click on admin select job dropdown selects job titles and add the given details and save it

# Job title details
JOBTITLE='Associate software engineer'
JOBDESCRIPTION='QUALITY ASSURANCE ENGINEER'
NOTE='This is a demo of how job title can be added'

class Test_orange_dashboard():

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

    def test_add_job_titles(self,test_invoke):
        wait=WebDriverWait(self.driver, 60)
        self.driver.find_element(By.CLASS_NAME, 'oxd-main-menu-item').click()
        h6TitleCheck=wait.until(Ec.presence_of_element_located((By.XPATH, '//h6[2]')))
        assert h6TitleCheck.text=='User Management'
        self.driver.find_element(By.XPATH, '//div[@class="orangehrm-header-container"]/button').click()
        h6TitleCheck1=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'h6')))
        assert h6TitleCheck1.text=='Admin'
        self.driver.find_element(By.XPATH, '//div[@class="oxd-topbar-body"]/nav/ul/li[2]').click()
        jobbtitles=wait.until(Ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a')))
        ActionChains(self.driver).move_to_element(jobbtitles).click().perform()
        h6TitleCheck2=wait.until(Ec.presence_of_element_located((By.XPATH, '//div[@class="orangehrm-header-container"]/h6')))
        assert h6TitleCheck2.text=='Job Titles'
        self.driver.find_element(By.XPATH, '//div[@class="orangehrm-header-container"]/div/button').click()
        h6TitleCheck3=wait.until(Ec.presence_of_element_located((By.XPATH, '//div[@class="orangehrm-card-container"]/h6')))
        assert h6TitleCheck3.text=='Add Job Title'
        self.driver.find_element(By.XPATH, '//div[@class="oxd-form-row"]/div/div/input').send_keys(JOBTITLE)
        self.driver.find_element(By.XPATH, '//div[@class="oxd-form-row"][2]/div/div[2]/textarea').send_keys(JOBDESCRIPTION)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/input').send_keys('/Users/niyogv/IdeaProjects/practice/orange/Screenshot 2024-03-19 at 12.24.24 PM.png')
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[2]/textarea').send_keys(NOTE)
        self.driver.find_element(By.XPATH, '//div[@class="oxd-form-actions"]/button[2]').click()
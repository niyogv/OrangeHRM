import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec

URL='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

# Test 1 submitting empty form
# Test 2 Submitting with only username
onlyuser='Admin'
# Test 3 submitting with only password
onlypassword='admin123'
# Test 4 submitting with invalid username and password
invaliduser='niyog'
invalidpassword='Test@123'
# Test 5 submitting with invalid username
invaliduseername='niyog'
validpassword='admin123'
# Test 6 submitting with invalid password
validuser='Admin'
invalidpass='Test@123'
# Test 7 submitting with valid cred
validname='Admin'
validpass='admin123'

class Test_login():

    @pytest.fixture
    def test_invoke(self):
        self.driver=webdriver.Chrome()
        self.driver.get(URL)

    def test_1(self,test_invoke):
        wait=WebDriverWait(self.driver, 60)
        button=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'button')))
        button.click()
        assert button.is_displayed()

    def test_2(self,test_invoke):
        wait=WebDriverWait(self.driver, 60)
        username=wait.until(Ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))
        username.send_keys(onlyuser)
        button=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'button')))
        button.click()
        assert button.is_displayed()

    def test_3(self,test_invoke):
        wait=WebDriverWait(self.driver, 60)
        password=wait.until(Ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
        password.send_keys(onlypassword)
        button=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'button')))
        button.click()
        assert button.is_displayed()

    def test_4(self,test_invoke):
        wait=WebDriverWait(self.driver, 60)
        username=wait.until(Ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))
        username.send_keys(invaliduser)
        password=wait.until(Ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
        password.send_keys(invalidpassword)
        button=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'button')))
        button.click()
        pTitleCheck=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'p')))
        assert pTitleCheck.text=='Invalid credentials'

    def test_5(self,test_invoke):
        wait=WebDriverWait(self.driver, 60)
        username=wait.until(Ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))
        username.send_keys(invaliduseername)
        password=wait.until(Ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
        password.send_keys(validpassword)
        button=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'button')))
        button.click()
        pTitleCheck=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'p')))
        assert pTitleCheck.text=='Invalid credentials'

    def test_6(self,test_invoke):
        wait=WebDriverWait(self.driver, 60)
        username=wait.until(Ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))
        username.send_keys(validuser)
        password=wait.until(Ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
        password.send_keys(invalidpass)
        button=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'button')))
        button.click()
        pTitleCheck=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'p')))
        assert pTitleCheck.text=='Invalid credentials'

    def test_7(self,test_invoke):
        wait=WebDriverWait(self.driver, 60)
        username=wait.until(Ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))
        username.send_keys(validname)
        password=wait.until(Ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
        password.send_keys(validpass)
        button=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'button')))
        button.click()
        h6TitleCheck=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'h6')))
        assert h6TitleCheck.text=='Dashboard'









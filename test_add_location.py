
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

# Base url
URL='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

# Login cred
USERNAME='Admin'
PASSWORD='admin123'

# Location details
NAME='NIYOG'
CITY='Bengaluru'
STATE='Karnataka'
ZIPCODE='560072'

def test_locations():
    driver=webdriver.Chrome()
    driver.get(URL)
    wait=WebDriverWait(driver, 60)
    username=wait.until(Ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))
    username.send_keys(USERNAME)
    password=wait.until(Ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
    password.send_keys(PASSWORD)
    button=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'button')))
    button.click()
    h6TitleCheck=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'h6')))
    assert h6TitleCheck.text=='Dashboard'
    driver.find_element(By.XPATH, '//ul[@class="oxd-main-menu"]/li[1]').click()
    h6TitleCheck=wait.until(Ec.presence_of_element_located((By.XPATH, '//span[@class="oxd-topbar-header-breadcrumb"]/h6')))
    assert h6TitleCheck.text=="Admin"
    driver.find_element(By.XPATH, '//div[@class="oxd-topbar-body"]/nav/ul/li[3]').click()
    loc=wait.until(Ec.presence_of_element_located((By.LINK_TEXT, 'Locations')))
    loc.click()
    h5TitleCheck=wait.until(Ec.presence_of_element_located((By.TAG_NAME, 'h5')))
    assert h5TitleCheck.text=='Locations'
    driver.find_element(By.XPATH, '//div[@class="orangehrm-header-container"]/div/button').click()
    h6TitleCheck1=wait.until(Ec.presence_of_element_located((By.XPATH, '//div[@class="orangehrm-background-container"]/div/h6')))
    assert h6TitleCheck1.text=='Add Location'
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input').send_keys(NAME)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys(CITY)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys(STATE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/div[2]/input').send_keys(ZIPCODE)
    driver.find_element(By.XPATH, '//div[@class="oxd-select-text oxd-select-text--active"]').click()
    driver.find_element(By.XPATH,'//div[@class="oxd-select-text oxd-select-text--active"]/div').click()
    driver.find_element(By.XPATH, '//div[@class="oxd-form-actions"]/button[2]').click()
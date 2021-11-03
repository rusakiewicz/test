from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

###############TEST 1 - Logowanie ####################
try:
    PATH = "D:\chromedriver.exe"
    driver = webdriver.Chrome(PATH) # or ...Chrome(executable_path=sciezka)
    driver.get("http://localhost:28558/")
    driver.maximize_window()
    time.sleep(2)
    log = driver.find_element_by_name('login')
    log.send_keys('m.stasiak@xopero.com')

    pas = driver.find_element_by_id('mat-input-1')
    pas.send_keys('Admin_123')

    driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/main/div/app-auth/div/app-auth-login/div/form/app-save-button/button').click()
    time.sleep(1)
    title = driver.current_url
    if title == 'http://localhost:28558/devices':
        print ("Test 1 - Logowanie: Pass")
    else:
        print("Test 1 - Logowanie: Failed")
except:
    print("Test 1 - Logowanie: Failed")

#################Test 2 - Dodawanie urządzenia#############
try:
    if driver.find_element_by_id("mat-badge-content-0").is_displayed():
        driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-toolbar-container/app-toolbar/mat-toolbar/mat-toolbar-row/div[2]/button[1]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="mat-checkbox-2"]/label/span[1]').click()
        driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-activate-devices-table/div/div[4]/app-save-button/button/span[1]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//app-license[2]/p').click()
        driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/div[1]/aside[2]/app-aside/ng-component/app-licenses-list/div/div[4]/app-save-button/button/span[1]/span').click()
        print('Test 2 - Dodawanie urządzenia: Pass')
    else:
        print('Test 2 - Dodawanie urządzenia: Pass(Brak urządzeń do dodania)')
except:
    print('Test 2 - Dodawanie urządzenia: Failed')


##############Test 3 - Dodawanie magazynu lokalnego##########

driver.find_element_by_xpath('/html/body/app-root/app-main/app-menu/section/nav[1]/a[6]').click()
driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-toolbar-container/app-toolbar/mat-toolbar/mat-toolbar-row/div[1]/ng-component/button/span[1]').click()
driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-storage/div/mat-form-field').find_element_by_xpath('//*[@id="mat-input-3"]').click()
# pwd_ele = driver.find_element_by_xpath('//*[@id="mat-input-3"]')
# print(pwd_ele.is_displayed()) #return true/false based on element status
# print(pwd_ele.is_enabled())
# pwd_ele.click()


time.sleep(2)
#driver.close()
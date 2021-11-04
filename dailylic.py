from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
    
    
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "D:\chromedriver.exe"
driver = webdriver.Chrome(PATH) # or ...Chrome(executable_path=sciezka)
driver.get("https://7975d7c0-3a18-4df8-9d94-3356898ba7c7.sin.xopero.com/")

driver.maximize_window()

driver.implicitly_wait(10)
#time.sleep(2)

##########|Logowanie###############
log = driver.find_element_by_name('login')
log.send_keys('m.stasiak+16349001459447672@xopero.com')
pas = driver.find_element_by_id('mat-input-1')
pas.send_keys('1Q2w3e4r.')
driver.find_element_by_xpath("//*[contains(text(),'Zaloguj się')]").click()
time.sleep(3)

driver.find_element_by_xpath("/html/body/app-root/app-main/div/app-content/main/div/ng-component/app-organizations/ng-containter/app-organization-container/app-organization/section/article/app-simplified-backup-plans/div/div/div/button/span[1]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(text(),'Git Protection')]").click()
# time.sleep(2)
print("Dodano plan do organizacji GIT")
try:
    time.sleep(1)
    driver.find_element_by_xpath("//*[contains(text(),'Start now')]").click()
    print("Uruchomiono plan backapu GIT")
except:
    print ("Błąd uruchamiania planu GIT")
    time.sleep(2)
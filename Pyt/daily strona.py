from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



PATH = "D:\chromedriver.exe"
driver = webdriver.Chrome(PATH) # or ...Chrome(executable_path=sciezka)
driver.get("https://xopero.com/pl/pobierz-xopero/")
driver.maximize_window()

driver.implicitly_wait(10)

TimeVar = str((time.time()))
MailVar = TimeVar.replace(".","")
PartEmail = ("m.stasiak+","@xopero.com")
Email = MailVar.join(PartEmail)

start = time.time()
firma = driver.find_element_by_name("company")
firma.send_keys("Xopero")
mail = driver.find_element_by_name("email")
mail.send_keys(Email)
phone = driver.find_element_by_name("phone")
phone.send_keys("123456789")

driver.find_element_by_xpath('//*[@id="top"]/div/div/div[2]/div/form/button').click()
driver.find_element_by_xpath('//*[@id="top"]/div/div/div[2]/div/form/div[5]/div/div/div/div[6]/button[2]').click()

driver.find_element_by_xpath('//*[@id="content-block"]/section[8]/div/div[2]/div/div[1]').click()
driver.get("https://mail.google.com")


stop = time.time()
Worktime = stop-start
print(Worktime)
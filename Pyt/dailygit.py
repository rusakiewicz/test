from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



PATH = "D:\chromedriver.exe"
driver = webdriver.Chrome(PATH) # or ...Chrome(executable_path=sciezka)
driver.get("https://gitprotect.io/")
driver.maximize_window()

TimeVar = str((time.time()))
MailVar = TimeVar.replace(".","")
PartEmail = ("m.stasiak+","@xopero.com")
Email = MailVar.join(PartEmail)

start = time.time()

##############Tworzenie konta gitprotect
driver.find_element_by_xpath('/html/body/section[1]/div/div/div[1]/div/a[1]').click()
firma = driver.find_element_by_name("login")
firma.send_keys(Email)
mail = driver.find_element_by_name("password")
mail.send_keys("1Q2w3e4r.")
phone = driver.find_element_by_name("companyName")
phone.send_keys("Xopero")
driver.find_element_by_xpath("//*[contains(text(),'Start now')]").click()

tworzenieKonta = 0
while driver.current_url == "https://gitprotect.io/sign-up.html":
    time.sleep(5)
    tworzenieKonta+=5
    print("Konto tworzy się", tworzenieKonta,"sekund")
title = driver.current_url
print(title)


############logowanie GIT
driver.implicitly_wait(10)
driver.get("https://github.com/")
time.sleep(2)
driver.find_element_by_xpath("//*[contains(text(),'Sign in')]").click()
time.sleep(2)
GH = driver.find_element_by_name("login")
GH.send_keys("stasiak.marek93@gmail.com")
PASY = driver.find_element_by_name("password")
PASY.send_keys("Plokijuh1.")
driver.find_element_by_name("commit").click()
time.sleep(1)
driver.get(title)

######Dodawanie organizacji GIT
try:
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('/html/body/app-root/app-main/app-first-run-container/app-first-run/section/div[2]/article[2]/button').click() #wybór git do utworzenia
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-git-organization/div/div[5]/app-save-button/button").click() #zatwierdzenie tworzenia git
    #try:
    print("Dodano organizację GitHub")
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
    #except:
        print("Nie Udało się dodać planu do organizacji GIT")
except:
    print("Nie udało się dodać organizacji GIT")

####################Kontrola Licencji
driver.implicitly_wait(2)
driver.find_element_by_xpath("//*[contains(text(),'Settings')]").click() #wybór ustawień
driver.find_element_by_xpath("//p[contains(.,'Manage your licenses')]").click() #wybór licencji
driver.find_element_by_xpath("//*[contains(text(),'See details')]").click() #wybór detali licencji
licencje = ['Microsoft 365','GitProtect','Feature worker','Server Agent','Endpoint Agent','Cloud worker','Virtual Agent per Host','Virtual Agent per Socket']
for lic in licencje:
    try:
        istrue = driver.find_element_by_xpath("//*[contains(text(),'%s')]" %(lic)).is_displayed()
        print("Dostępność licencji %s = " % (lic),istrue)
    except:
        print("Dostępność licencji %s = " % (lic),"False")

#########Kontrola workera i magazynu
driver.find_element_by_xpath("//*[contains(text(),'Storages')]").click() #wybór magazynu
time.sleep(1)
print('Dostępność magazynu xopero: ', driver.find_element_by_xpath("//*[contains(text(),'Xopero Storage #1')]").is_displayed())

driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/main/div/ng-component/app-storages-page/article/app-table/cdk-virtual-scroll-viewport/div[1]/table/tbody/tr/td[5]/button').click()
print('Dostępność cloud workera: ',driver.find_element_by_xpath("//*[contains(text(),'Cloud Worker')]").is_displayed())


driver.find_element_by_xpath("//*[contains(text(),'Tasks')]").click() #wybór zadań

#kontrola zakończenia zadania backup
time.sleep(2)
x = True
while x:
    if driver.find_element_by_id('mat-badge-content-5').is_displayed():
        time.sleep(5)
        print("Buckup w trakcie wykonywania")
    else:
        x = False
driver.find_element_by_xpath("//*[contains(text(),'Last 24 hours')]").click() #wybór wykonanych zadań
time.sleep(10)
#Kontrola przywróconych backupów
driver.find_element_by_xpath('/html/body/app-root/app-main/app-menu/section/nav[1]/a[2]').click()
#time.sleep(30)
plany = 0
driver.find_element_by_xpath("/html/body/app-root/app-main/div/app-content/main/div/ng-component/app-organizations/ng-containter/app-organization-container/app-organization/section/footer/button[2]").click()
time.sleep(2)
for i in range(1,11):
    driver.find_element_by_xpath("/html/body/app-root/app-main/div/app-content/main/div/ng-component/app-repositories/article/app-table/cdk-virtual-scroll-viewport/div[1]/table/tbody/tr[%d]/td[7]/button[2]/span[1]" %(i)).click()
    time.sleep(5)
    try:
        driver.find_element_by_xpath("//*[contains(text(),'View available plans, then select the backup copy to restore')]").is_displayed()
        print("Brak planu backup")
    except:
        print("Plan backup dostępny")
        plany+=1

print("Utworzono ", plany, "na 10 planów")

#####uruchomienie backupu
driver.implicitly_wait(5)
driver.find_element_by_xpath('/html/body/app-root/app-main/div/app-content/div[1]/aside/app-aside/ng-component/app-resource-backups/div/div[3]/div/app-browser-container/app-browser/div/div/app-browser-backups/div/div/div[2]/div/button').click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(text(),'Restore all')]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(text(),'Start now')]").click()

driver.find_element_by_xpath("//*[contains(text(),'Tasks')]").click() #wybór zadań
time.sleep(2)
x = True
while x:
    if driver.find_element_by_id('mat-badge-content-5').is_displayed():
        time.sleep(5)
        print("Buckup w trakcie wykonywania")
    else:
        x = False
driver.find_element_by_xpath("//*[contains(text(),'Last 24 hours')]").click() #wybór wykonanych zadań
print("Wykonano przywracanie repozytorium")

stop = time.time()
Worktime = stop-start
print(Worktime)


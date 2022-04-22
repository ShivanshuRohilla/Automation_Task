import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


s = Service("C:/DevLop/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)

Action_Obj = ActionChains(driver)
'''Open Brower'''
driver.get("https://account.xunison.com/")

'''Maximize window'''
driver.maximize_window()

Find_Login = driver.find_element(by=By.XPATH, value='(//input[@class="form-control ng-untouched ng-pristine ng-invalid"])[1]')
Find_Login.send_keys("soham.c@xunison.com") #Login

Find_Pass = driver.find_element(by=By.XPATH, value='//input[@type="password"]')
Find_Pass.send_keys("soham123") #Password

#Enter
driver.find_element(by=By.XPATH, value='/html/body/app-root/mat-sidenav-container/mat-sidenav-content/app-login-page/div/div/div[2]/div/div/div/form/button[1]').send_keys(Keys.ENTER)
time.sleep(3)

#Select Value
driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div/mat-dialog-container/app-select-gateway/div/div/div[2]/div/div[2]/button').click()
time.sleep(2)
driver.find_element(by=By.XPATH, value='//p[text()="Smart Home"]').click()
time.sleep(2)

Click_Setting = driver.find_element(by=By.XPATH, value='(//div[@class="mat-list-item-content"])[2]')
Action_Obj.move_to_element(Click_Setting).perform()

driver.find_element(by=By.XPATH, value='//*[text()="Settings"]').click() #Click Setings
time.sleep(1)

driver.find_element(by=By.XPATH, value='/html/body/app-root/mat-sidenav-container/mat-sidenav-content/app-settings/div/div/div[2]/app-network-information/div/div[3]/div/div[2]/div[1]/div[1]/ng-select/div/div/div[3]/input').send_keys("Kolkata")
time.sleep(1)
driver.find_element(by=By.XPATH, value='/html/body/app-root/mat-sidenav-container/mat-sidenav-content/app-settings/div/div/div[2]/app-network-information/div/div[3]/div/div[2]/div[1]/div[1]/ng-select/div/div/div[3]/input').send_keys(Keys.ENTER)

driver.find_element(by=By.XPATH, value='//button[@class="text-white bg-green x-button br-0 mat-flat-button mat-button-base"]').click()

#Close the browser
driver.close()

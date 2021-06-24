from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from path import *

def waitUntilVisibility(path):
    wait = WebDriverWait(driver, 1000)  #waiting for expected conditions
    wait.until(ec.visibility_of_element_located((By.XPATH, path)))

def disableCamMic(mic,cam):
    waitUntilVisibility(mic)
    print(1)
    driver.find_element_by_xpath(mic).click()
    print(2)
    waitUntilVisibility(cam)
    print(3)
    driver.find_element_by_xpath(cam).click()
    print(4)
    time.sleep(1)

def join(joinbutton):
    waitUntilVisibility(joinbutton)
    print(5)
    driver.find_element_by_xpath(joinbutton).click()
    print(6)

def goToUrl(meetcode):
    url = f"https://meet.google.com/{meetcode}"
    driver.get(url)

def markAttendence(message,chatbutton,textarea,sendbutton):
    waitUntilVisibility(chatbutton)
    driver.find_element_by_xpath(chatbutton).click()
    print(7)

    waitUntilVisibility(textarea)
    driver.find_element_by_xpath(textarea).send_keys(message)
    print(8)

    waitUntilVisibility(sendbutton)
    driver.find_element_by_xpath(sendbutton).click()
    print(9)



meetcode = str(input("Input Meet Code >>  ")) #input from user
message = str(input("Message >>  "))


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Chandan\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
wait = WebDriverWait(driver, 1000)



goToUrl(meetcode)
disableCamMic(mic,cam)
join(joinbutton)
markAttendence(message,chatbutton,textarea,sendbutton)








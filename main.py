from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from path import *
import speech_recognition as sr
import pyaudio

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
    time.sleep(5)
    driver.find_element_by_xpath(chatbutton).click()
    print(7)

    waitUntilVisibility(textarea)
    driver.find_element_by_xpath(textarea).send_keys(message)
    print(8)

    waitUntilVisibility(sendbutton)
    driver.find_element_by_xpath(sendbutton).click()
    print(9)

    waitUntilVisibility(chatbutton)
    driver.find_element_by_xpath(chatbutton).click()
    print(10)

def recognizeVoice(name):
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        if (dev['name'] == 'Stereo Mix (Realtek(R) Audio)' and dev['hostApi'] == 0):
            dev_index = dev['index']
            print('dev_index', dev_index)

    while(True):

        r = sr.Recognizer()
        print(1)


        with sr.Microphone(device_index=dev_index) as source:

            audio = r.listen(source)
            print(2)
            MyText = r.recognize_google(audio, language = 'en-IN', show_all = True)
            print(3)
            text = MyText.get('alternative')
            a = text[0]
            recognizedVoice = a['transcript'].lower()
            print(recognizedVoice)

            if name in recognizedVoice:
                markAttendence(message,chatbutton,textarea,sendbutton)
            else:
                pass



meetcode = str(input("Input Meet Code >>  ")) #input from user


name = str(input('Your Name>> ')).lower()
message = str(input("Message >>  "))


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Chandan\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
wait = WebDriverWait(driver, 1000)



goToUrl(meetcode)
time.sleep(5)
disableCamMic(mic,cam)
time.sleep(5)
join(joinbutton)
time.sleep(5)
markAttendence(message,chatbutton,textarea,sendbutton)
time.sleep(5)
recognizeVoice()








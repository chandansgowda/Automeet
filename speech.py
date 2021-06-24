from selenium import webdriver 
from time import sleep 
import speech_recognition as sr 
import pyaudio


# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     dev = p.get_device_info_by_index(i)
#     if (dev['name'] == 'Stereo Mix (Realtek(R) Audio)' and dev['hostApi'] == 0):
#         dev_index = dev['index']
#         print('dev_index', dev_index)
while(True):

    r = sr.Recognizer()
    print(1)


    with sr.Microphone(device_index=1) as source2:

        audio2 = r.listen(source2)
        print(2)
        MyText = r.recognize_google(audio2, language = 'en-IN', show_all = True)
        print(3)
        text = MyText.get('alternative')
        a = text[0]

        print(a['transcript'])
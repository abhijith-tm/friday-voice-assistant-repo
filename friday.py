import cv2
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import random
import wikipedia
import webbrowser
import sys
import pyjokes
import pyautogui
import time
import instaloader
import pywhatkit
import PyPDF2
from tkinter.filedialog import *


# speech recognition is imported and renamed as sr for easy use
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[2].id)


# defining a function to convert text to speech

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#  To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}')

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


# To wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour > 0 and hour <= 12:
        speak('good morning')
    elif hour > 12 and hour < 18:
        speak('good afternoon')
    else:
        speak('good evening')
    speak('i am friday. sir please tell me how can i help you')


# to get current time
def xtime():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


# to get news
def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=35ab651459ea426aab0664002b5b6250"

    main_page = requests.get(main_url).json()
    # print main page
    articles = main_page["articles"]
    # print articles
    head = []
    day = ["first", "second", "third", 'fourth', 'fifth', 'sixth', "seventh", "eighth", 'ninth', "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's (day[i) news is: ", head[i
        speak(f"today's {day[i]} news is: , {head[i]}")


# TO READ PDF
def pdf_reader():
    speak("sir,please select the book")
    book = askopenfile()
    pdf_Reader = PyPDF2.PdfFileReader(book)
    pages = pdf_Reader.numPages
    speak(f"Total numbers of pages  in this book {pages}  ")
    speak("sir please enter the page number i have to read")
    pg = int(input("please enter the page number :"))
    page = pdf_Reader.getPage(pg)
    text = page.extractText()
    speak(text)

def quiz(self):

        quistions = ['1. Who is known as the father of Free Software Foundation?',
                     '2. In which year was the "C" programming language developed?',
                     '3.Who is known as the father of Internet?',
                     '4.Who used the binary system of numeration for the first time?',
                     '5.Who is the first computer programmer?', '6.In which year was computer graphics oringinated?',
                     '7.Who is the inventor of Supercomputer?', '8.What is the name of Worlds first digital Computer?',
                     '9.What is the name of Indian first indigenous supercomputer developed by CDAC named?',
                     '10.Which was the first Pocket Computer?',
                     '11.What is the name of the tablet introduced by Amazon?', '12.Who invented Computer Mouse?',
                     '13.Speak to Tweet is a service given by which giant?',
                     '14.Xoom is the name of tablet developed by which company?',
                     '15. WIT is the NASDAW code of which Indian IT company?', '16.Expand HDMI',
                     '17.What was developed by PYRA Labs and later sold to google?',
                     '18.Who is known as the father of World Wide Web?',
                     '19.Which mehod is used to connect to a remote computer?',
                     '20.What do you call a single point on a computer screen?',
                     '21.The CPU Chip used in a computer is made of which element?',
                     '22.Which computer was designed to be compact as possible?',
                     '23.What is the name of the device which produce hard copy graphics?',
                     '24.When is world computer literacy day celebrated?',
                     '25.The processing power of a CPU is measured in?', '26.Windows 10 was released on which day?',
                     '27.Which command is used to view the sub directory structure of a drive?',
                     '28.Round robin scheduling is he premptive version of?',
                     '29.When did IBM released its first version of DOS OS 1.0?',
                     '30.Start button was introduced in which operating system?',
                     '31.Groupon was rebranded in India to what name?',
                     '32.Which system software does the job of merging the records from two files to one?',
                     '33.While running DOS on a computer, which command is used to duplicate the entire diskette?',
                     '34.What is the name given to the organized collection of software that control the entire operation of c computer?',
                     '35.What is the name of the OS for the laptop MACLITE?',
                     '36.What is the memory range from 1k-640k called?',
                     '37.IBM released its first PC in 1981, what was the name of OS that was popular at that time?',
                     '38.How long is an IPV6 Address?', '39.Which protocol does DHCP uses at the transport layer?',
                     '40.Which protocol is used to send a destination network unknown messge back to originating host?',
                     '41.Which WLAN IEEE Specification allows upto 54 mbps at 2.4 Ghz?',
                     '42.Which protocol does PPP uses to identify the network layer protocol?', '43.HBA Stands for?',
                     '44.What is the second generation of the Web called?',
                     '45. If you have a CISCO Mesh network , what protocl allows multiple APÃ¢â‚¬â„¢s to connect with many redundant connection between nodes?',
                     '46.Which protocol is used to identify the hardware address of a local device?',
                     '47. PAT Address translation is also termed as what?',
                     '48. When was the term Social Networking first used?', '49.Who founded Ã¢â‚¬ËœmyspaceÃ¢â‚¬â„¢?',
                     '50.Which social media allows a user to create map of exactly where a photo was taken?',
                     '51.What type of audience are primarily in a social network?',
                     '52.Twitter is an example of what service?',
                     '53.What is the character limit for a tweet in Twitter?',
                     '54.What was the largest social network prior to facebook?',
                     '55. Which social network does not have followers?',
                     '56.When was the social networking first become popular online?',
                     '57. Which is used to search and browse for information online?',
                     '58.What is Youtubes Slogan?', '59.P2P,B2B, and B2C are part of?',
                     '60. Winchester drive is also called as what?',
                     '61.What kind of connectors are used to connect a PC power supply to a hardware?',
                     '62.What is the term Wave Table Synthesis related to?',
                     '63.What type of memory is Pendrive?', '64.Which IRQ does the hard disk drive use?',
                     '65.Who invented Compact disc?', '66.What is Arrandale code name for?',
                     '67.What hardware was used by the initial generation of computers?',
                     '68. Which was the first computer made available for commercial use?',
                     '69.Name the first mechanical computer designed by Charles Babbage called',
                     '70.The concentric circles on the platter of hard disk is known as?',
                     '71.IRQ6 is commenly assigned to?',
                     '72.Which component in a PC regulated the color depth and screen resolution of a monitor?',
                     '73. A Computer programming language for simulating models of business activity is?',
                     '74.The words that are set aside by the programming language for its own use is called as what?',
                     '75.Which programming language is used for scientific calculations?',
                     '76.Which computer language is used on the Internet?',
                     '77.Which language is used for the developedment of various games?',
                     '78.Which language was devised by Dr, Seymour Papart?',
                     '79. Which computer language is used for Artificial Intelligence?',
                     '80.Who is the creator of PASCAL language?',
                     '81.A systems programming language for micro computers in the Intel family is called?',
                     '82. Which language is more suited to a structured program?',
                     '83.MS/DOS is written in which language?',
                     '84. A program element that allows structuring of a program in a different way is called?',
                     '85. A name given by Intel to high speed MOS technology is called?',
                     '86. Who is the new CEO of Flipkart.com ?']
        answers = ['Richard Mathew Stallman', '1972', 'Vinton Cerf', 'Thomas Harriot', 'Ada Lovelace', '1940',
                   'Seymour Cray',
                   'Mark 1', 'Param', 'SHARP PC1211', 'Kindle Fire', 'Doughles Engelbert', 'Google', 'Motorola',
                   'Wipro',
                   'High Defenition Multimedia Interface', 'Blogger', 'Tim Berners Lee', 'Dialup', 'Pixel', 'Silica',
                   'Micro Computer', 'Plotter', 'December 2', 'MIPS', 'July 29', 'TREE', 'FIFO', '1981', 'Windows 95',
                   'Nearbuy', 'Utility Program', 'DISKCOPY', 'Operating System', 'OZ', 'Conventional memory', 'CP/M',
                   '128 bit (16 byte)', 'UDP', 'ICMP', 'IEEE 802.11G', 'NCP', 'Host Bus Adapter', 'Web 2.0', 'AWPP',
                   'Address Resolution Protocol', 'NAT Overload', '1954', 'Tom Anderson', 'Flickr', 'Joiners', '140',
                   'myspace',
                   'Google Plus', '2003', 'Netscape', 'Broadcast Yourself', 'Share Economy', 'Hard disk drive', 'Molex',
                   'Sound', 'Flash Memory', '14', 'James Russel', 'Intel Processor', 'Valves', 'UNIVAC',
                   'Analytical Engine',
                   'Tracks', 'Floppy Drive Controller', 'VRAM', 'GPSS', 'Control Structures', 'FORTRAN', 'Java', 'C++',
                   'LOGO',
                   'Prolog', 'Niclaus Wirth', 'PC/M', 'PASCAL', 'C++', 'Co-Routine', 'HMOS']


        n = 0
        i = 0
        score = 0
        life = 4
        try:
            while True:
                print(quistions[n])
                if life == 0:
                    speak('You lose')
                    break
                ans = input('<^> :')
                if ans.lower() == answers[n].lower():
                    print('correct')
                    life = life + 1
                    print('life: ', life)
                    score = score + 1
                else:
                    score = score - 1
                    life = life - 1
                    print("Ans: ", answers[n])
                    print('wrong')
                    print('life: ', life)
                n = n + 1
                i = i + 1
        except:
            speak(f'your score is ', score)



 # control speed of voice

def speed():
        speak("sir ,should i increase or decrease the speed")
        sp = takecommand().lower()
        try:
            if sp == 'increase':
                engine.setProperty('rate', 150)
                engine.runAndWait()
            elif sp == 'decrease':
                engine.setProperty('rate', 70)
                engine.runAndWait()
        except:
            pass



 # logic building for tasks

if __name__ == "__main__":  # speak('hello sir')

    wish()



    while True:

        query = takecommand().lower()
        # logic building for tasks

        if 'open notepad' in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "close notepad" in query:
            speak("okay sir ,closing the application")
            os.system("taskkill /f /im notepad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt" in query:
            speak("okay sir ,closing the application")
            os.system("taskkill /f /im cmd.exe")

        elif "open cmd" in query:
            os.system("start cmd")

        elif "close cmd" in query:
            speak("okay sir ,closing the application")
            os.system("taskkill /f /im cmd.exe")

        elif "open whatsapp" in query:
            wpath = "C:\\Users\\Lenovo\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.system(wpath)

        elif "close whatsapp" in query:
            speak("okay sir ,closing the application")
            os.system("taskkill /f /im whatsapp.exe")

        elif "open chrome" in query:
            cpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.system(cpath)

        elif "close chrome" in query:
            speak("okay sir ,closing the application")
            os.system("taskkill /f /im chrome.exe")

        elif "open opera" in query:
            opath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Opera\\launcher.exe"
            os.system(opath)

        elif "close opera" in query:
            speak("okay sir ,closing the application")
            os.system("taskkill /f /im launcher.exe")

        elif "open telegram" in query:
            tpath = "C:\\Users\\Lenovo\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.system(tpath)

        elif "close telegram" in query:
            speak("okay sir ,closing the application")
            os.system("taskkill /f /im Telegram.exe")

        elif "open vs code" in query:
            vpath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.system(vpath)

        elif "close vs code" in query:
            speak("okay sir ,closing the application")
            os.system("taskkill /f /im code.exe")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "D:\\jarvis_project\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "wikipedia" in query:
            speak("searching wikipedia......")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif "search on youtube" in query:
            speak("sir,what should i search")
            search = takecommand().lower()
            pywhatkit.playonyt(f"{search}")

        elif "open stackoverflow" in query:
            webbrowser.open('www.stackoverflow.com')

        elif "what time is it" in query:
            xtime()

        elif "search on google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            pywhatkit.search(f"{cm}")

        elif "you can sleep" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")
            speak("shut downing system..")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
            speak("restarting system")

        elif "sleep this system" in query:
            os.system("rundll32.exe powrproof.dll,setsuspendstate 0,1,0")

        elif "switch window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me the news" in query:
            speak("please wait sir, fetching the news")
            news()

        elif "where i am" in query or "where we are" in query:
            speak('wait sir,let me check')
            try:
                ipADD = requests.get('https://api.ipify.org').text
                url = 'https://get.geojs.io/v1/ip/geo/' + ipADD + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo data)
                city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f"sir iam not sure, i think we are in {city} city of {state} state of  {country} country")
            except Exception as e:
                speak("sorry sir,due to network issue iam not able to find where we are")
                pass

        elif "instagram profile" in query or "profile on instagram" in query:

            speak("sir please enter the user name correctly.")
            name = input('Enter username here: ')
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(1)
            speak("sir would you like to download profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()  # instadownloader library
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile picture is saved in our main folder")

        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir, tell me the name the name for the screenshot")
            name = takecommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak(" i am done sir,the screenshot is saved in our main folder")

        # elif "read pdf" in query: not working need to fix the function
        #     pdf_reader()
        elif "change speed of voice" in query or "change voice speed" in query or "voice speed" in query:  # woking,need little more work
            speed()

        elif "thank you" in query:
            speak("it's my pleasure sir")

        elif "do calculations" in query or "can you calculate":
            pass

        elif "play a game" in query:
            speak("ok sir, starting quiz")
            quiz()
            speak("sir, do you want to try again")
            inp = input('   ').lower()
            if inp == 'yes':
                quiz()

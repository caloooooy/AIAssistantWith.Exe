import pyttsx3 #pip install pyttsx3 
import datetime #add datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib #simple mail transfer protocol library
import webbrowser as wb #webbrowser 
import psutil #pip install psutil #process and system utilities
import pyjokes #pip install pyjokes
import os #operating systems
import pyautogui #pip install pyautogui 

engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S") 
    speak("Ang oras ngayon ay")
    speak(Time)
def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("Ang petsa ngayon ay")
    speak(month)
    speak(day)
    speak(year)
def wishme():
    speak("Welcome back Master Carlo")
    time()
    date()

    #Greetings
    hour = datetime.datetime.now().hour
    if hour >=6 and hour < 12:
        speak("Magandang Umaga Master Carlo!")
    elif hour >= 12 and hour < 18:
        speak("Magandang Hapon Master Carlo!")
    elif hour >= 18 and hour < 24:
        speak("Magandang Gabi Master Carlo")
    else:
        speak("Matulog ka na Master Carlo")

    speak("Swane ang inyong lingkod. Ano ang maitutulong ko ngayon?")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('Ang inyong computer ay'+ usage +'na lamang')

    battery = str(psutil.sensors_battery())
    speak('Ang inyong computer ay'+ battery +'na lamang')
    

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    #emailsend
    server.login('username@gmail.com','password')
    server.sendmail('username@gmail.com',to,content)
    server.close()

def jokes():
    speak(pyjokes.get_joke())

def ss():
    img = pyautogui.screenshot()
    img.save('C:/Users/Swane/Desktop/img/screenshot.png')

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Nakikinig....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("Pakiulit master....")
        return "None"
    return query







if __name__ == "__main__":
    
    wishme()

    #All commands will be stored in lower case
    while True:
        query = TakeCommand().lower()
        if 'time' in query: #Swane will tell time
            time()
        
        elif 'date' in query: #Swane will tell date 
            date()

        elif 'wikipedia' in query: #Swane search
            speak("Searching....")
            query=query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=1)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif 'send email' in query: #Swane send email
            try:
                speak("Ano ang sasabihin ko?")
                content = TakeCommand() 
                #receiver
                speak("Sino ang aking bibigyan ng mensahe?")
                receiver = input("Pagbibigyan ng mensahe: ")
                to = receiver
                sendEmail(to,content)
                speak(content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak("Unable to send Email")

        elif 'chrome' in query: #Swane will chrome
            speak('Ano ang aking hahanapin?')
            chrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chrome).open_new_tab(search+'.com')
        
        elif 'search youtube' in query: 
            speak('Ano ang aking hahanapin?')
            search_Yt = TakeCommand().lower()
            speak("HAHAHAHAHAHA....Youtube")
            wb.open('https://www.youtube.com/results?search_query='+search_Yt)

        elif 'search google' in query: #Swane
            speak('Ano ang aking hahanapin?')
            search_chrome = TakeCommand().lower()
            speak("HAHAHAHA Google")
            wb.open('https://www.google.com/search?q=')

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query: 
            jokes()

        elif 'go sleep' in query:
            speak('Matutulog na ako master')
            quit()
            
        elif 'game' in query:
            speak('Maglalaro ka na')
            valorant = r'C:/Riot Games/Riot Client/RiotClientServices.exe'
            os.startfile(valorant)

        elif 'dota' in query:
            speak('Masusunod')
            dota = r'C:/Program Files (x86)/Steam/steam.exe'
            os.startfile(dota)
        
        elif 'write a note' in query:
            speak('Ano ang sasabihin ko, Master?')
            notes = TakeCommand()
            file = open('sulat.txt', 'w')
            speak('Isama ko pa yung Araw at Oras?')
            answer = TakeCommand()
            if 'yes' in answer or 'sure' in answer:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Tapos na Master!')
            else:
                file.write(notes)


        elif 'show notes' in query:
            speak('Ipapakita ko na')
            file = open('sagot.txt', 'r')
            print(file.read())
            speak(file.read())
        
        elif 'screenshot' in query:
            ss()
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternnon! ")
    else:
        speak("Good Evening! ")   
    speak(" Hello Sir my name is LUCIFER Memory one terabyte Speed 2 tetrahertz. Please Tell me How may i help you")
def takeCommand():
    '''It takes microphone input from the user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please .....")
        return "None"
    return query    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nssrivas@gmail.com', 'password')
    server.sendmail('nssrivas@gmail.com',to,content)
    server.close()
if _name_ == '_main_':
    wishMe()
    while True:
        query = takeCommand().lower()
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences=2)
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open online c compiler' in query:
            webbrowser.open("onlinegdb.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open vs code' in query:
            codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'brave browser' in query:
            codePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codePath)
        elif 'email to ns' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "nssrivas@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print((e))
                speak("Sorry Sir I am not able to send this mail")
        elif 'exit' in query:
            exit()
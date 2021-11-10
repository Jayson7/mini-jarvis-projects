import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import pyjokes

import os
import smtplib
import pywhatkit
engine = pyttsx3.init("espeak")
voices = engine.getProperty('voices')
# print(voices[11].id)
engine.setProperty('voice', voices[11].id)
# engine.say("hello jayson")
# engine.runAndWait()
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
 
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
 
    else:
        speak("Good Evening!")  
 
    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output
 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
 
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
 
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
 
# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('lexxiijoo70@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()
  
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
 
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'who is' in query:
            person = query.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)
        
        elif 'joke' in query:
            speak("okay sir but you must laugh")
            speak(pyjokes.get_joke())

#  /////
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
 
 
        # elif 'play music' in query:
        #     music_dir = '/home/jayson/Downloads'
        #     songs = os.listdir(music_dir)
        #     print(songs)    
        #     os.startfile(os.path.join(music_dir, songs[0]))
 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        # elif 'quick maths' in query:
        #     speak("okay sir go ahead")

        #     print(query)
        #     speak(f"Sir, the time is {strTime}")
        

        # elif 'open code' in query:
        #     codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(codePath)
 
        # elif 'email to friend' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "yourfriendEmail@gmail.com"   
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry. I am not able to send this email") 
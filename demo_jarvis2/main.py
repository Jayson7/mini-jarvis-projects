import pyttsx3 
import jarvis
import datetime
import speech_recognition as sr


r = sr.Recognizer()
engine = pyttsx3.init()

# talk
def speak(audio):

    engine.say(audio)
    engine.runAndWait()


# timer

def timer():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

# date

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(year)
    speak(month)
    speak(day)

# greetings

def greeter():
    speak("Hello Jayson")
    speak("the current time is") 
    timer()  
    speak( '  and the current date is ') 
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("good morning jayson")
    elif hour >= 12 and hour< 18:
        speak("good afternoon jayson")
    elif hour >= 18 and hour<24:
        speak("good evening jayson")
    else:
        speak("good morning jayson, why are you not asleep, how may i help")

    speak( " i'm Jarvis, please tell me how i can help")
greeter()

def command():
    
    with sr.Microphone() as source:
        print("Listening sir")
        r.pause_threshold =1 
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-us")
            print(query)
        except Exception as e:
            print(e)
            speak("say that again please")
            return "None"
        return query 



command()


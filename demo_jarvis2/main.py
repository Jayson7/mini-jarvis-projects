import pyttsx3 
import jarvis
import datetime
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
    speak("the current time is " + timer())  
    speak( '  and the current date is ' + date())
    speak( " i'm Jarvis, please tell me how i can help")


greeter()
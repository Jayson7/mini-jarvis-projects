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

timer()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(year)
    speak(month)
    speak(day)

date()

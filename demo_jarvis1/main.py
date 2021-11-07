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


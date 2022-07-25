import speech_recognition as sr
import pyttsx3 as p


engine=p.init()
r=sr.Recognizer()
voices=engine.getProperty('voices')
rate=engine.getProperty('rate')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 100)
engine.say('Hello how are you doing?')

engine.runAndWait()
print('Say something')
with sr.Microphone() as source:
   
    audio=r.listen(source)
    try:
        voice_data=r.recognize_google(audio)
        print(voice_data)
    except sr.UnknownValueError:
        print('sorry')   
    

import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 120)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            r.adjust_for_ambient_noise(source, duration=1)  
            audio = r.listen(source)
            content = r.recognize_google(audio, language='en-in')
            print("You said: " + content)
            return content.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except Exception as e:
            print(f"Error: {e}")
            return ""

def main_process():
    speak("hello i am your friend avika")
    
    while True:
        request = command()

        if request == "":
            continue  

        if "hello" in request:
            speak("how may i help you")
        
        elif "can you play my favourite music" in request:
            speak("ok bro playing your favourite song")
            webbrowser.open("https://www.youtube.com/watch?v=Zg19wRDBhX8&list=RDZg19wRDBhX8&start_radio=1")
        elif "girlfriend" in request:
            speak("paras single hai")        
        elif "time" in request:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"The current time is {current_time}")
            speak(f"The current time is {current_time}")
        
        elif "email" in request:
            speak("Opening Email")
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

        elif "website" in request:
            speak("Opening Pisoft Informatics Private Limited")
            webbrowser.open("https://www.pisoftinformatics.com/pisoft/")
        
        elif "google" in request:
            speak("Opening Google for you")
            webbrowser.open("https://www.google.com/")

        elif "exit" in request or "quit" in request or "stop" in request:
            speak("bui bui")
            break

        else:
            search_url = f"https://www.google.com/search?q={request.replace(' ', '+')}"
            speak(f"Searching Google for {request}")
            webbrowser.open(search_url)

main_process()

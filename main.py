import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):

    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")

    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")

    elif "open github" in c.lower():
        webbrowser.open("https://github.com")

    elif "open icai" in c.lower():
        webbrowser.open("https://icai.org")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=1d48058e72174be8838da644a55bd4b5")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

if (__name__ == "__main__"):
    speak("Activating Jarvis....")

    while True:

        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                print("waiting for the wake word...")
                audio = r.listen(source,timeout=3,phrase_time_limit=2)
            word = r.recognize_google(audio)
            print("Recognising...")
            if ("jarvis" in word.lower()):
                speak("Jarvis activated!")
                speak("Ya How can i help you")
                with sr.Microphone() as source:
                    print("Listening the command...")
                    audio = r.listen(source,timeout=4,phrase_time_limit=2)
                    command = r.recognize_google(audio)
                print(command)

                processCommand(command)
            
        except Exception as e:
            print("Jarvis error",e)
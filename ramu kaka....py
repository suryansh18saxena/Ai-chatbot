import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    # Function to speak a given text
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google"in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook"in c.lower():
        webbrowser.open("http://facebook.com")
    elif "open youtube"in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open linkedin"in c.lower():
        webbrowser.open("http://linkedin.com")
    elif "open instagram"in c.lower():
        webbrowser.open("http://instagram.com")
    elif "open tech news"in c.lower():
        webbrowser.open("https://www.gadgets360.com/news")
    elif "open gpt"in c.lower():
        webbrowser.open("https://chatgpt.com/")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=b0f7165dbcc74155826980ef1461b170")
        
        if r.status_code==200:
            data=r.json()
            articles = data.get('articles',[])
            for article in articles:
                speak(article['title'])

if __name__ == "__main__":
    speak("ramu kaka aarahe hai ...")
    print("boliya mailk")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=3)
            
            # Recognize speech using Google's recognizer
            command = recognizer.recognize_google(audio)
            if (command.lower()=="ramu kaka"):
                speak("boliya sir")
                with sr.Microphone()as source:
                    print("ramu kaka aagaye")
                    audio=recognizer.listen (source)
                    command=recognizer.recognize_google(audio)

                    processcommand(command)

        except Exception as e:
            print(f"An error occurred: {e}")

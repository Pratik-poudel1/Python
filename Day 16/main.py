import speech_recognition as sr
import webbrowser
import pyttsx3
import music

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

recognizer = sr.Recognizer()

def open_site(url):
    webbrowser.get('chrome').open(url)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        open_site("https://google.com")
        speak("Opening Google")
    elif "open youtube" in c.lower():
        open_site("https://youtube.com")
        speak("Opening YouTube")
    elif "open facebook" in c.lower():
        open_site("https://facebook.com")
        speak("Opening Facebook")
    elif "open instagram" in c.lower():
        open_site("https://instagram.com")
        speak("Opening Instagram")
    elif "open twitter" in c.lower():
        open_site("https://twitter.com")
        speak("Opening Twitter")
    elif "open linkedin" in c.lower():
        open_site("https://linkedin.com")
        speak("Opening LinkedIn")
    elif "open github" in c.lower():
        open_site("https://github.com")
        speak("Opening GitHub")
    elif "open stackoverflow" in c.lower():
        open_site("https://stackoverflow.com")
        speak("Opening Stack Overflow")
    elif "open tiktok" in c.lower():
        open_site("https://tiktok.com")
        speak("Opening TikTok")
    elif "open twitch" in c.lower():
        open_site("https://twitch.com")
        speak("Opening Twitch")
    elif "open reddit" in c.lower():
        open_site("https://reddit.com")
        speak("Opening Reddit")
    elif "open amazon" in c.lower():
        open_site("https://amazon.com")
        speak("Opening Amazon")
    elif "open gmail" in c.lower():
        open_site("https://gmail.com")
        speak("Opening Gmail")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play ", "")
        open_site(music.music[song])
        speak("Playing " + song)
    elif c.lower().startswith("search"):
        search = c.lower().replace("search ", "")
        open_site("https://google.com/search?q=" + search)
        speak("Searching for " + search)
    elif "good bye" in c.lower():
        speak("Good bye sir !")
        exit()
    else:
        speak("I'm sorry, I don't understand")
    


if __name__ == "__main__":
    speak("Initializing Junior......")

    while True:
        # Listen for the wake word "Junior"
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("Recognizing...")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)
            print("Heard:", word)
            if "junior" in word.lower():
                speak("Yes sir?")
                # Listen for command
                with sr.Microphone() as source:
                    print("Junior Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
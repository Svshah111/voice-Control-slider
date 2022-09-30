import pyttsx3
import speech_recognition as sr
import pyautogui
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty ('rate')
engine.setProperty('rate', 130)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        #print("Say that again please...")  
        return "None"
    return query
def next_page():
    pyautogui.press('right')
def back_page():
    pyautogui.press('left')

def Friday_AI():

    while True:

        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif'next' in query:
            next_page()
        elif'back' in query:
            back_page()

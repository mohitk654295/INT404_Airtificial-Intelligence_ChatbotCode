import wikipedia
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
engine = pyttsx3.init('sapi5')              #speech application programming interface
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():                                          #wishME module will wish the user at startup
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening sir")
    speak("I am Angel. How may I help you Sir")

def TakeCommand():                                     #this will take the command from user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recogonizing...")
        query = r.recognize_google(audio, language='en-in')         
        print(f"User said: {query}\n")
    except Exception as e:
       # print(e)
        print("Say that again please...")
        return "None"
    return query
    
if __name__ == "__main__":
    wishMe()
    #while True:                     # ...bot will listen in infinite loop
    if 1 :                             #chat bot will run in finite mode....can be changed 
        query = TakeCommand().lower()
    #logic for creating tasks
        if 'who is ' in query:
            speak("Searching Wikipedia...")
            query = query.replace("who is ","")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia") 
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube for you")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google for you")
            webbrowser.open("google.com")
        elif 'open geeks for geeks' in query:
            speak("opening geeks for geeks for you")
            webbrowser.open("geeksforgeeks.org")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        elif 'code' in query:
            speak("opening visual studio for you")
            codePath = "C:\\Users\\Mohit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open notepad' in query:
            speak("opening notepad for you")
            codePath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(codePath)
        elif 'how are you' in query:
            speak("I am fine sir, how about you")
            query=TakeCommand().lower()
            if 'i am good' in query:
                speak("Thats good to hear sir")
            else:
                speak("okay sir")
        elif 'search' in query:
            query=query.replace("search","")
            speak("here are some results")
            webbrowser.open('https://google.com/search?q=' + query)
            results= wikipedia.summary(query, sentences=1)
            speak(results)
        elif 'open youtube and play' in query:
          #  query=query.replace("open youtube and ","")
            speak("showing you some resuts")
            webbrowser.open('https://youtube.com/search?v=' + query)
            speak("you can play the song by clicking on it........enjoy")
        elif 'write in notepad' in query:
            speak("What should I write, sir?")
            note_text = TakeCommand().lower()
            with open("notepad.txt", "w") as f:
                f.write(note_text)
                speak("I have written it in notepad, sir.")
        elif 'who are you' in query :
            speak("basically I am a chat bot based on cloud computing. I was programmed by engineer mohit kumar.")
 
        elif 'hello' in query:
            speak("Hello sir...how may i assist you")
        else:
            speak("Could you say that again please.")


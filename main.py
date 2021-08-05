from youtubesearchpython import *
import webbrowser
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

# Loop infinitely for user to speak
while(1):    
    try:
        with sr.Microphone() as source:
            print("start")
            #listens for the user's input 
            r.adjust_for_ambient_noise(source,duration=0.2)
            audio = r.record(source, duration=3)
            # Using google to recognize audio
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()
            print(MyText)

            if MyText == "benjamin":
                SpeakText("Hi What song")
                r.adjust_for_ambient_noise(source,duration=0.2)
                song = r.record(source, duration=3)
                song_name = r.recognize_google(song,language="en-US")
                song_name = song_name.lower()
                print(song_name)

                customSearch = CustomSearch(song_name, VideoSortOrder.viewCount)
                url = customSearch.result()['result'][0]['link']
                webbrowser.open(url)
              
    except sr.RequestError as e: pass
          
    except sr.UnknownValueError: print("Don't Understand")
 
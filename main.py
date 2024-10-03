import speech_recognition as sr #used for recognizing speech
from selenium import webdriver  #used to control web browser
import urllib.parse             #used for managing URLs

class Voice:    #this class will have the methods for listening through the mic and processing voice commands
    def __init__(self):
        self.recognizer = sr.Recognizer()   #recognizer is the instance of voice class to which Recognizer class from the sr library is assigned
        self.microphone()   #instance of microphone class called
    
    def microphone(self):   
        while True: #infinite loop that keeps on listening and processing 
            try:    #handle any exceptions
                with sr.Microphone() as source: #uses microphone class from the sr library. it opens the microphne for listening and 'with' ensures that the microphone is properly managed
                    print("Listening...")
                    audio = self.recognizer.listen(source)  #listens to the microphone audio and captures it
                    command=self.recognizer.recognize_google(audio).lower() #converts the audio to text
                    print(command)
                    if 'hey google' in command:
                        print("Hey! how are you doing today?")

                    if 'search' in command:
                        search_query = command.split('search ')[-1]
                        encoded_query = urllib.parse.quote_plus(search_query)
                        url = f"https://www.google.com/search?q={encoded_query}"
                        driver = webdriver.Chrome() #initializes a new instance of the chrome webdriver
                        driver.get(url) #navigates to the desired result webpage

            except sr.UnknownValueError:    #catches exception if the speech recognizer doesnt recognizes it
                print("Sorry, I didn't catch that. Try again!")
                break

listener = Voice()  #listener is the object and it is calling the instance of the Voice class

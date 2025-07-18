import speech_recognition as sr

# import webbrowser
# import pyttsx3
# import musicLibrary
# import requests

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()
# newsapi = "47e7a7affcf14054a77ecfa23e10ce48"

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def processCommand(c):
#     if "open google" in c.lower():
#         webbrowser.open("https://google.com")
#     elif "open youtube" in c.lower():
#         webbrowser.open("https://youtube.com")
#     elif "open facebook" in c.lower():
#         webbrowser.open("https://facebook.com")
#     elif "open instagram" in c.lower():
#         webbrowser.open("https://instagram.com")
#     elif c.lower().startswith("play"):
#         song = c.lower().split(" ")[1]
#         link = musicLibrary.music.get(song)
#         if link:
#             webbrowser.open(link)
#         else:
#             speak("Song not found.")

#     elif "news" in c.lower():
#         r=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=47e7a7affcf14054a77ecfa23e10ce48") 
#         if r.status_code == 200:
#             data = r.json() #Parse the json response 
#             articles = data.get('articles', [])

#             #print headlines 
#             for x in articles:
#                 speak(x['title'])   
#     else:
#         #let open AI handle the request
#         pass             

    
    
    

        


# if __name__ == "__main__":
#     speak("Initialising Robo....")
#     #Listen for the word robo to start
#     while True:
#         #Obtain audio from microphone
#         r = sr.Recognizer()
        

#         #recognize speech 
#         try:
#             with sr.Microphone() as source :
#                 print("Listening ....")
#                 audio = r.listen(source , timeout= 2 ,  phrase_time_limit = 1)
#             word = r.recognize_google(audio)
#             print(word)
#             if(word.lower() == "robo"):
#                 speak("yes , how can I help you")
#                 #Listen for command
#                 with sr.Microphone() as source:
#                     print("Robo active")
#                     audio = r.listen(source)
#                     command = r.recognize_google(audio)


#                     processCommand(command)
#         except Exception as e:
#             print(e)    
#         except sr.WaitTimeoutError:
#             print("Timeout. No speech detected.")        









import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.  
        
    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned  
    return query 
dict={'ayushi':'gargaayushi547@gmail.com'}
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gargaayushi547@gmail.com', 'tswlvviwdzougwhl')
    server.sendmail('gargaayushi547@gmail.com', to, content)
    server.close()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
        
    speak("I am Jarvis Sir.Please tell me how may I help you")       
    
if __name__ == "__main__":
   wishMe()
   if 1:
      query=takeCommand().lower()
      if 'wikipedia' in query:
          speak("searching wikipedia....")
          query=query.replace("wikipedia","")
          results=wikipedia.summary(query,sentences=2)
          speak("According to wikipedia")
          print(results)
          speak(results)
          
      elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")  
        
      elif 'open google' in query:
        webbrowser.open("https://www.google.com")    
        
      elif 'open satckoverflow' in query:
        webbrowser.open("https://www.stackoverflow.com") 
        
      elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))  

      elif ' time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
      elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)     
            
      elif 'email' in query:
        try:
            speak("Whom should I send the email?")
            recipient_name = takeCommand().lower()

            # Check if recipient_name exists in the dictionary
            recipient_email = dict.get(recipient_name)

            if recipient_email is not None:
               speak("What should I say in the email?")
               content = takeCommand()
               if content is not None:
                sendEmail(recipient_email, content)
                speak("Email has been sent!")
               else:
                  speak("Sorry, the email content is empty. Email not sent.")
            else:
               speak("Sorry, I couldn't find the recipient's email address.")
            
        except Exception as e:
            print("Say that again please...")   #Say that again will be printed in case of improper voice 

 
                
      elif 'jarvis quit' in query or 'exit' in query or 'close' in query:
        speak("Thank you for using Jarvis.")
        exit()            
            
            
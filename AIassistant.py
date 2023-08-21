import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

r = sr.Recognizer()
phone_numbers = {"Ravi": "8812", "Sneha":"23233", "Yawalak": "377783", "papa": "10069420"}
def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening Now.........")
            audioin = r.listen(source)
            my_text = r.recognize_google(audioin)
            my_text = my_text.lower()
            print(my_text)
#play song
            if 'play' in my_text:
                my_text = my_text.replace('play', '')
                speak('Playing' + my_text)
                pywhatkit.playonyt(my_text)
#date time
            if 'date' in my_text:
                today = datetime.date.today()
                times = datetime.datetime.now().strftime('%H : %M')
                speak("Today is" )
                speak(today)
                speak("and the time is")
                speak(times)
# ask details
            if "who is" in my_text:
                person = my_text.replace('who is', '')
                info = wikipedia.summary(person, 2)
                speak(info)
#ask phone numbers
            if "call" in my_text:
                numberr = list(phone_numbers)
                print(numberr)
                for numberr in numberr:
                    if numberr in my_text:
                        print(numberr + "'s phone number is "+ phone_numbers(numberr))
                        speak(numberr + "'s phone number is "+ phone_numbers(numberr))
    except:
        print("Error") 
speak("Welcome Boss")
commands()
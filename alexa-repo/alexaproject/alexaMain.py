print("Hello World")

import speech_recognition as sr
import pyttsx3 #getting alexa to talk to you by creating engine#text to speech
#import pywhatkit
import datetime
import wikipedia
import pyjokes
#import pyowm
import webbrowser
import pyaudio


listener = sr. Recognizer()
engine = pyttsx3.init() #initializing the engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume',2.0)
engine.setProperty('LanguageCode',"en-US")
#engine.setProperty('voice',)

def talk(text):
    engine.say(text) #makes it dynamic
    #engine.say('What can I do for you')
    engine.runAndWait()
def take_command():
    command='Nothing'
    try:
        with sr.Microphone() as source:
            print('listening...') #shows if alexa is listening
            voice = listener.listen(source) #calling on the listener to listen to the source
            listener.adjust_for_ambient_noise(source)
            listener.dynamic_energy_threshold = 3000
            command = listener.recognize_google(voice) #google api speech for text gives you text version of what you spoke
            command = command. lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                #print(command) #print or command
            else:
                try:
                    input('Press enter to exit.')
                except:
                    command="error"
    except sr.WaitTimeoutError:
        pass
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        pass
    return command

def run_alexa(command=" "):
    if not command:
        command = take_command() #take command's output
    if 'jala' in command:
        song = command.replace('play', '')
        talk('playing' + song)
       # pywhatkit.playonyt(song) #playing on youtube
        print(song)
    elif 'created you' in command:
        talk("Alula you dumbass")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S:%p')
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info= wikipedia.summary(person, 1)
        talk(info)
    elif 'date' in command:
        talk('sorry, i have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif "tell me about yourself" in command:
        talk("I am Alexa and I am your personal assistant")
        pass
    elif "play" in command:
        #talk("Opening Youtube.")
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        #url='https://www.youtube.com/'search?q{}".format(command)
        #new=2
        #webbrowser.open_new("https://www.youtube.com/search?q{}".format(command)
        #webbrowser.get(using='google-chrome').open(url,new=new)
        #webbrowser.get(chrome_path).open(url)
        command = command.replace('play', '')
        song=command
        talk('playing' + song)
        webbrowser.open("https://www.youtube.com/search?q={}".format(song))
        pass
    elif "facebook" in command:
        talk("opening facebook.")
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        url = 'https://www.facebook.com/'
        webbrowser.get(chrome_path).open(url)
        pass
    elif "where is" in command:
        command=command.replace("where is",'')
        talk("finding you the location")
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        url ='https://www.google.com/maps/place/search?q={}'.format(command)
        webbrowser.get(chrome_path).open(url)
        pass

    elif "feeling" in command:
        talk("i am good")
        pass
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        pass
    elif 'bestfriend' in command:
        talk("you dumbass")
        pass
    elif 'stop' in command:
        pass
    else:
        talk('please say something else')
        pass

DEFAULT=True
while DEFAULT:
    command=take_command()
    if 'stop' in command:
        DEFAULT = False
    else:
        run_alexa(command)

#it will keep on running even after you ask a question

#covnversation_log='Conversation log.txt'




import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia 

# Receive audio from microphone and return a transcription 

def transform_audio_text():

    # Instaciar recognizer
    r = sr.Recognizer()

    # Microphone configuration
    with sr.Microphone() as origin:

        # waiting time
        r.pause_threshold= 0.8
        print('Im listening')

        # Save transcription
        audio= r.listen(origin)

        try:
            # Search in google
            request= r.recognize_google(audio, language='en-us')
            print(f'You said: {request}')
            return request

        except sr.UnknownValueError:
            print('Ops, I didnt get that')
            return 'Im still listening'

        except sr.RequestError:
            print('Ops, no service')
            return 'Im still listening'

        except:
            print('Ops, something went wrong')
            return 'Im still listening'


# Receive and say a given message
def talk(message):

    # Start pyttsx3 engine
    engine = pyttsx3.init()
    # Set English as language
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
    engine.say(message)
    engine.runAndWait()


# Report day and week
def report_day():

    day= datetime.date.today()

    day_of_the_week= day.weekday()

    d_days = {0:'Monday',
              1:'Tuesday',
              2:'Wednesday',
              3:'Thursday',
              4:'Friday',
              5:'Saturday',
              6:'Sunday'}
    talk(f'Today is {d_days[day_of_the_week]}')


# Report time
def report_time():

    time = datetime.datetime.now()
    print(time)
    talk(f"Right now, it's {time.hour} {time.minute}")


# Welcome
def welcome():

    # Recognize time
    time = datetime.datetime.now()
    if time.hour<6 or time.hour>20:
        greeting = 'Good Evening!'
    elif 6<= time.hour < 13:
        greeting='Good Morning!'
    else:
        greeting='Good Afternoon'
    
    talk(f"{greeting}. I'm David, your virtual assistant. How can I help?")


# Main
def main():

    welcome()
    start=True
    while start:
        request=transform_audio_text().lower()
        if 'open youtube' in request:
            talk('Right away, opening youtube')
            webbrowser.open('https://www.youtube.com')
            continue

        elif 'open the browser' in request:
            talk('Sure, opening browser.')
            webbrowser.open('https://www.google.com')
            continue

        elif 'what day is today' in request:
            report_day()
            continue

        elif 'what time is it' in request:
            report_time()
            continue

        elif 'search in wikipedia' in request:
            talk('Ok, searching')
            request = request.replace('search in wikipedia', '')
            wikipedia.set_lang('en')
            result = wikipedia.summary(request, sentences=1)
            talk(f'I found this. {result}')
            continue

        elif 'search' in request:
            talk("Ok, I'm on it")
            pywhatkit.search(request)
            talk('This is what I found')
            continue

        elif 'play' in request:
            talk("Nice, I'm on it")
            pywhatkit.playonyt(request)
            continue

        elif 'joke' in request:
            talk(pyjokes.get_joke('en'))
            continue
        
        elif 'stock prices' in request:
            action=request.split('of')[-1].strip()
            wallet={'apple': 'APPL',
                    'amazon': 'AMZN',
                    'google':'GOOGL'}
            try: 
                action_searched= wallet[action]
                action_searched=yf.Ticker(action_searched)
                actual_price=action_searched.info['regularMarketPrice']
                talk(f'I found it, the price of {action} is {actual_price}')
            except:
                talk("I'm sorry, I did not found it")
        
        elif 'see you soon' in request:
            talk("I don't wanna go Mr. Stark")
            start=False
            break

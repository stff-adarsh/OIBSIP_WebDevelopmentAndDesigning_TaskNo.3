import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speaking speed

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)  # Reduce background noise
        audio = r.listen(source, timeout=5, phrase_time_limit=7)  # Avoid infinite waiting

    try:
        command = r.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""
    except sr.RequestError:
        speak("Sorry, speech service is down.")
        return ""
    except Exception as e:
        speak(f"Error: {str(e)}")
        return ""

def respond(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time_now}")
    elif "date" in command:
        date_today = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today's date is {date_today}")
    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "search" in command:
        speak("What do you want to search for?")
        query = listen()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the results for {query}")
    elif "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I don't know that command.")

def run_assistant():
    speak("Voice Assistant is ready.")
    while True:
        command = listen()
        if command:
            respond(command)

if __name__ == "__main__":
    run_assistant()

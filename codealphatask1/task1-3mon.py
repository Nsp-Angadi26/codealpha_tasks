import speech_recognition as sr
import pyttsx3
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand that.")
        return None
    except sr.RequestError:
        speak("Network error. Please check your internet connection.")
        return None

def respond(command):
    if "wikipedia" in command:
        topic = command.replace("wikipedia", "").strip()
        speak(f"Searching Wikipedia for {topic}")
        try:
            summary = wikipedia.summary(topic, sentences=2)
            speak(summary)
        except wikipedia.exceptions.DisambiguationError:
            speak("Multiple results found. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("No matching results found.")
    elif "hello" in command:
        speak("Hello! How can I assist you?")
    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm not sure how to respond to that.")

if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            respond(command)

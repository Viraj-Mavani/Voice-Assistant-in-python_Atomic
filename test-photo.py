import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
from googlesearch import *
import webbrowser
import logo
from ecapture import ecapture as ec

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):

	print("Atomic : ", audio)
	engine.say(audio)
	engine.runAndWait()

def takeCommand():

	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Listening...")
	    r.pause_threshold = 0.6
	    # r.operation_timeout = 5
	    audio = r.listen(source, phrase_time_limit=5)

	try:
	    print("Recognizing...")
	    query = r.recognize_google(audio, language='en-in')
	    print(f"User said: {query}\n")

	except Exception as e:
		speak("Could not understand your audio, PLease try again !")
		return "None"
	return query


if __name__ == "__main__":
	logo.atomic_logo()

	#wishMe()
	# while True:

	speak("Tell me")
	# query = takeCommand().lower()
	query = "tack a photo"
	# query = "stop"

	if 'exit' in query or 'bye' in query or 'see you later' in query or 'stop' in query:
		speak("As you wish, Anything for you.")
		exit()

	elif ("capture" in query or "photo" in query) and "photo" in query:
		ec.capture(0,"Atmoic","img.jpg")

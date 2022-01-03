import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
from googlesearch import *
import webbrowser
import datetime
# from path import path
import os
import logo

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
	# query = "Note that i have made a note."
	query = "define yourself"
	# query = "stop"

	if 'exit' in query or 'bye' in query or 'see you later' in query or 'stop' in query:
		speak("As you wish, Anything for you.")
		exit()

	elif "note" in query or "remember this" in query:
		speak("What would you like me to write down?")
		# note_text = takeCommand()
		note_text = "For some types of queries, Wolfram|Alpha decides that although it can provide some results"
		# note_text = "speak pandu is gandu"
		date = str(datetime.datetime.now()).replace("-","")
		date = date.replace(" ", "")
		date = date.replace(":", "")
		date = date.replace(".", "")
		print(date)
		# directory = "F:\\Python\\Mini_project\\Reminders\\"
		directory = os.path.abspath("Mini_project/Reminders/Note_")
		# path("Mini_project/Reminders/").abspath()
		file_name = date[0:15] + "_" + note_text[0:15] + "... .txt"
		filepath = directory + file_name
		with open(filepath, "w") as f:
			f.write(str(datetime.datetime.now()) + "\n\n" + note_text)
		print(directory)
		print(file_name)
		speak("I have made a note of that.")

	elif "speak" in query:
		query = query.replace("speak","").strip()
		speak(query)
		# speak(query)

	elif "who are you" in query or "define yourself" in query or 'what can you do' in query:
		info = '''Hello, I am Your personal Assistant, Atomic 1 point O.\n\tI am here to make your life easier. You can command me\n\tto perform various tasks such as opening youtube,google
	chrome, google and gmail ,i can predict time, take a photo,\n\tsearch wikipedia, predict weather in different cities, get\n\ttop headline news from times of india and you can ask me
	computational or geographical questions too!'''
		speak(info)

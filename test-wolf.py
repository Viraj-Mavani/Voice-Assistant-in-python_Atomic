import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
from googlesearch import *
import webbrowser
import logo
import wolframalpha

# "weather" 5762390d8cb1516821df61a1f94b98a9
# "wolf" TAH989-5R4GQ7E6TT
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
	query = "what is the time"
	# query = "what is the temperature in rajkot"
	# query = "calculate one plus one"

	if 'exit' in query or 'bye' in query or 'see you later' in query or 'stop' in query:
		speak("As you wish, Anything for you.")
		exit()

	elif "calculate" in query:
		app_id = "Wolframalpha api id"
		client = wolframalpha.Client("TAH989-5R4GQ7E6TT")
		indx = query.lower().split().index('calculate')
		query = query.split()[indx + 1:]
		res = client.query(' '.join(query))
		answer = next(res.results).text
		speak("The answer is " + answer)

	elif "what is" in query or "who is" in query:

		# Use the same API key
		# that we have generated earlier
		client = wolframalpha.Client("TAH989-5R4GQ7E6TT")
		res = client.query(query)

		try:
			speak (next(res.results).text)
		except StopIteration:
			# speak("No Result")
			speak(f"Searching {query} in google")
			webbrowser.open("https://google.com/search?q=" + query)
			speak("Here is your result.")

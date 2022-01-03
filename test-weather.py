import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
from googlesearch import *
import webbrowser
import logo
import requests
from bs4 import BeautifulSoup

# query = "weather" 5762390d8cb1516821df61a1f94b98a9
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
	while True:

		speak("Tell me")
		# query = takeCommand().lower()
		query = "what is the temperature in rajkot"

		if query == 0:
			continue

		elif 'exit' in query or 'bye' in query or 'see you later' in query or 'stop' in query:
			speak("As you wish, Anything for you.")
			exit()

		elif "weather" in query:
			api_key="5762390d8cb1516821df61a1f94b98a9"
			base_url="https://api.openweathermap.org/data/2.5/weather?"
			speak("Whats the city name?")
			city_name=takeCommand()
			complete_url=base_url+"appid="+api_key+"&q="+city_name
			response = requests.get(complete_url)
			x=response.json()
			if x["cod"]!="404":
				y=x["main"]
				current_temperature = y["temp"]
				current_humidiy = y["humidity"]
				z = x["weather"]
				weather_description = z[0]["description"]
				speak(" Temperature in kelvin unit is " + str(current_temperature) + "\n humidity in percentage is " + str(current_humidiy) + "\n description  " + str(weather_description))
			else:
				speak(" City Not Found ")

		elif "what is" in query or "the" in query and "temperature" in query:
			city_wo_what = query.replace("what is","").strip()
			city_wo_what = city_wo_what.replace("the","").strip()
			city = city_wo_what.replace("temperature in","").strip()
			search = "temperature in "+ city
			url = f"https://www.google.com/search?q={search}"
			r = requests.get(url)
			data = BeautifulSoup(r.text,"html.parser")
			temp = data.find("div",class_="BNeawe").text; print(city); print(f"current temperature in {city} is {temp}")


		# elif "weather" in query:
		# 	api_key="5762390d8cb1516821df61a1f94b98a9"
		# 	base_url="https://api.openweathermap.org/data/2.5/weather?"
		# 	speak("Whats the city name?")
		# 	city_name=takeCommand()
		# 	complete_url=base_url+"appid="+api_key+"&q="+city_name
		# 	response = requests.get(complete_url)
		# 	x=response.json()
		# 	if x["cod"]!="404":
		# 		y=x["main"]
		# 		current_temperature = y["temp"]
		# 		current_humidiy = y["humidity"]
		# 		z = x["weather"]
		# 		weather_description = z[0]["description"]
		# 		speak(" Temperature in kelvin unit is " + str(current_temperature) + "\n humidity in percentage is " +
		# 				str(current_humidiy) + "\n description  " + str(weather_description))
		# 	else:
		# 		speak(" City Not Found ")

		# elif "what is" in query or "the" in query and "temperature" in query:
		# 	city_wo_what = query.replace("what is","").strip()
		# 	city_wo_what = city_wo_what.replace("the","").strip()
		# 	city = city_wo_what.replace("temperature in","").strip()
		# 	search = "temperature in "+ city
		# 	url = f"https://www.google.com/search?q={search}"
		# 	r = requests.get(url)
		# 	data = BeautifulSoup(r.text,"html.parser")
		# 	temp = data.find("div",class_="BNeawe").text
		# 	speak(f"current temperature in {city} is {temp}")

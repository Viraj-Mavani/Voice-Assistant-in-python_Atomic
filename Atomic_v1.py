import logo
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import random
import webbrowser
import os
import winshell
import smtplib
import subprocess
# from selenium import webdriver
import playsound
from gtts import gTTS
import wolframalpha
import ctypes
import pyjokes
import wmi
from ecapture import ecapture as ec
import requests
from bs4 import BeautifulSoup

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
		r.threshold = 1
		r.pause_threshold = 0.6
		r.operation_timeout = 25
		audio = r.listen(source, phrase_time_limit=25)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		speak("Could not understand your audio, PLease try again !")
		return "None"
	return query

# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour >= 0 and hour < 12:
#         speak("Good Morning!")
#
#     elif hour >= 12 and hour < 18:
#         speak("Good Afternoon!")
#
#     else:
#         speak("Good Evening!")
#
#     speak("I am your personal A.I. Assitant, Atomic")


if __name__ == "__main__":
	logo.atomic_logo()

	#wishMe()
	try:
		while True:

			speak("What can i do for you?")
			query = takeCommand().lower()


			if query == 0:
				continue
			elif "shutup" in query or "shut up" in query:
				speak("aye aye sir!")
				break
			# elif "don't listen" in query or ("stop" in query and "listening" in query) or "do not listen" in query:
			# 	speak("For how many seconds do you want me to sleep")
			# 	try:
			# 		a = int(takeCommand())
			# 		time.sleep(a)
			# 		speak(f"{str(a)} seconds completed. Now you can ask me anything")
			# 	except Exception as e:
			# 		speak("Please Tell me the number of seconds only!")
			# 		break

			elif 'exit' in query or 'bye' in query or 'see you later' in query or 'stop' in query:
				speak("As you wish, Anything for you.")
				break


			elif "open youtube" in query:
				speak("opening Youtube")
				webbrowser.open_new_tab("https://www.youtube.com")
				speak("youtube is open now")
			elif 'open google' in query:
				speak("opening Google")
				webbrowser.open_new_tab("https://www.google.com")
				speak("Google is open now")
			elif 'open gmail' in query:
				speak("opening Google mail")
				webbrowser.open_new_tab("gmail.com")
				speak("Google Mail open now")
			elif 'news' in query:
				news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
				speak('Here are some headlines from the Times of India, Happy reading')


			elif 'open' in query:
				try:
					if "stack overflow" in query:
						speak("Bro I can understand")
						webbrowser.open_new_tab("https://stackoverflow.com/")
						speak("Here you go to Stack Over flow. Happy coding")
					elif "chrome" in query:
						speak("Opening Google Chrome")
						os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
					elif "brave" in query:
						speak("Opening Brave")
						os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")
					elif "firefox" in query or "mozilla" in query:
						speak("Opening Mozilla Firefox")
						os.startfile("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
					elif "microsoft" in query and "edge" in query:
						speak("Opening Microsoft Edge")
						os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
					elif "discord" in query:
						speak("Opening Discord")
						os.startfile("C:\\Users\\LENOVO\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe")
					elif "word" in query:
						speak("Opening Microsoft Word")
						os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word 2016')
					elif "powerpoint" in query:
						speak("Opening Microsoft PowerPoint")
						os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint 2016')
					elif "excel" in query:
						speak("Opening Microsoft Excel")
						os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel 2016')
					elif "atom" in query or "IDE" in query:
						speak("Opening Atom")
						os.startfile('C:\\Users\\LENOVO\\AppData\\Local\\atom\\atom.exe')
					elif "code" in query or "VS" in query:
						speak("Opening VS Code")
						# os.startfile("C:\\Program Files\\Microsoft VS Code\\Code.exe")
						os.startfile("C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
					else:
						speak("Application not available")
						continue
				except Exception as e:
					speak("Location not found please try again")


			elif "who are you" in query or "define yourself" in query or 'what can you do' in query:
				info = '''Hello, I am Your personal Assistant, Atomic 1 point O.\n\tI am here to make your life easier. You can command me\n\tto perform various tasks such as opening youtube,google
	chrome, google and gmail ,i can predict time, take a photo,\n\tsearch wikipedia, predict weather in different cities, get\n\ttop headline news from times of india and you can ask me
	computational or geographical questions too!'''
				speak(info)
			elif "who made you" in query or "who created you" in query:
				speak("I have been created by Viraj Mavani.")
			elif "what's your name" in query or "what is your name" in query:
				speak("My friends call me Atomic")
			elif 'how are you' in query:
				speak("I am fine, Thank you")
				speak("How are you, Sir")
				if 'fine' in query or "good" in query:
					speak("It's good to know that your fine")
				else:
					continue


			elif "speak" in query:
				query = query.replace("speak","").strip()
				speak(query)
			# elif ("capture" in query or "photo" in query) and "photo" in query:
			# 	ec.capture(0,"robo camera","img.jpg")

			elif "toss" in query and "coin" in query:
				coinResult = random.randint(0,1)
				if coinResult == 0 :
					speak("Its a Head!")
				else :
					speak("Its Tails!")
			elif 'joke' in query:
				speak(pyjokes.get_joke())
			elif "empty" in query and "recycle bin" in query:
				try:
					winshell.recycle_bin().empty(
						confirm=True, show_progress=False, sound=True
					)
				except Exception as e:
					speak("Maybe, Bin is aleardy empty")
					break
				speak("Recycle Bin Emptied")
			elif "change" in query and "wallpaper" in query or "background" in query:
				img = r"C:\Users\Lenovo\Downloads\Wallpaper"
				list_img = os.listdir(img)
				imgChoice = random.choice(list_img)
				randomImg = os.path.join(img, imgChoice)
				ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
				speak("Background changed successfully")
			elif "where is" in query:
				ind = query.lower().split().index("is")
				location = query.split()[ind + 1:]
				url = "https://www.google.com/maps/place/" + "".join(location)
				speak("This is where " + str(location) + " is.")
				webbrowser.open(url)
			elif "note" in query or "remember this" in query:
				speak("What would you like me to write down?")
				note_text = takeCommand()
				date = str(datetime.datetime.now()).replace("-","")
				date = date.replace(" ", "")
				date = date.replace(":", "")
				date = date.replace(".", "")
				directory = os.path.abspath("Reminders/Note_")
				file_name = date[0:15] + "_" + note_text[0:15] + "... .txt"
				filepath = directory + file_name
				with open(filepath, "w") as f:
					f.write(str(datetime.datetime.now()) + "\n\n" + note_text)
				speak("I have made a note of that.")


			elif "calculate" in query:
				app_id = "Wolframalpha api id"
				client = wolframalpha.Client("KEY")
				indx = query.lower().split().index('calculate')
				query = query.split()[indx + 1:]
				res = client.query(' '.join(query))
				answer = next(res.results).text
				speak("The answer is " + answer)


			elif 'the time' in query:
				strTime = datetime.datetime.now().strftime("%H:%M:%S")
				speak(f"Sir, the time is {strTime}")


			elif ('wikipedia' in query and 'search' in query) or ('wikipedia' in query):
				speak('Searching Wikipedia...')
				query = query.replace("wikipedia", "")
				results = wikipedia.summary(query, sentences=2)
				speak("According to Wikipedia")
				speak(results)
				more_info="Want to know more?"
				speak(more_info)
				more_info_query = takeCommand().lower()
				if "yes" in more_info_query or "yeah" in more_info_query:
					speak("Opening Wikipedia")
					# query = query.replace("in wikipedia", "")
					# query = query.replace("wikipedia", "")
					# query = query.replace("search", "").strip()
					webbrowser.open("https://en.wikipedia.org/wiki/" + (query))
					speak(f"Here is more information about {query}")

				else:
					speak("ok")
					continue

			elif "system" in query and ("information" in query or "specs" in query or "specification" in query):
				c = wmi.WMI()
				my_system = c.Win32_ComputerSystem()[0]

				speak(f"Manufacturer: {my_system.Manufacturer}")
				speak(f"Model: {my_system. Model}")
				speak(f"Name: {my_system.Name}")
				speak(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
				speak(f"SystemType: {my_system.SystemType}")
				speak(f"SystemFamily: {my_system.SystemFamily}")

			elif "what is" in query or "who is" in query or "weather" in query:
				client = wolframalpha.Client("KEY")
				res = client.query(query)
				try:
					speak(next(res.results).text)
					speak("Anything else?")
					more_info_query = takeCommand()
					if "yes" in more_info_query or "yeah" in more_info_query:
						# speak("Then...")
						continue
					elif "no" in more_info_query:
						speak("Ok, Thanks for having me")
						break
				except StopIteration:
					# speak("No Result")
					speak(f"Searching {query} in google")
					webbrowser.open("https://google.com/search?q=" + query)
					speak("Here is your result.")


			elif 'youtube' in query or 'play' in query:
				query = query.replace("play ", "")
				query = query.replace("in youtube", "")
				query = query.replace("on youtube", "").strip()
				speak(f"playing {query} in youtube")
				api_key = "KEY"
				from apiclient.discovery import build
				# query= query.split("play")
				# query = str(query[0: ])
				youtube = build("youtube" , "v3" , developerKey = api_key)
				query = youtube.search().list(q = query ,part="id",type="video",fields="items/id")
				query = query.execute()
				query = query['items'][0]['id']['videoId']
				webbrowser.open("https://www.youtube.com/watch?v=" + query)
				speak("Enjoy, sir")
				break


			elif 'google' in query or 'search' in query:
				query = query.replace("search", "")
				query = query.replace("in google", "")
				query = query.replace("google", "")
				query = query.replace("on google", "").strip()
				speak(f"searching {query} in google")
				webbrowser.open("https://google.com/search?q=" + query)
				speak("Here is your result.")
				speak("Anything else?")
				more_info_query = takeCommand()
				if "yes" in more_info_query or "yeah" in more_info_query:
					speak("Then...")
					continue
				else:
					speak("Ok, Thanks for having me")
					break



			elif "lock the pc" in query or "lock the screen" in query:
				speak("Ok , locking your pc")
				ctypes.windll.user32.LockWorkStation()
				# subprocess.run(["ls", "-l"])
				# subprocess.call(["rundll32.exe user32.dll, LockWorkStation"])
				break

			elif "log off" in query or "sign out" in query:
				speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
				subprocess.call(["shutdown", "/l"])
				break

			elif "shutdown" in query and ("pc" in query or "laptop" in query or "device" in query):
				speak("Ok , your pc will shutdown in 10 sec make sure you exit from all applications")
				# subprocess.call(["shutdown", "/s", "/t", "10")
				os.system("shutdown /s /t 10")
				break

			elif "restart" in query and ("pc" in query or "laptop" in query or "device" in query):
				speak("Ok , your pc will restart in 10 sec make sure you exit from all applications")
				# subprocess.call(["shutdown", "/r", "/t", "10")
				os.system("shutdown /r /t 10")
				break

			else:
				if 'none' in query:
					continue
				else:
					speak(f"Searching {query} in google")
					webbrowser.open("https://google.com/search?q=" + query)
					speak("Here is your result.")
					speak("Anything else?")
					more_info_query = takeCommand()
					if "yes" in more_info_query or "yeah" in more_info_query:
						speak("Then...")
						continue
					else:
						break

	except Exception as e:
		speak("Oh...I think I need my MEDIC, something wrong happened with me.")

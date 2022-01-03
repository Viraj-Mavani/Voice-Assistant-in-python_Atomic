import wikipedia
import webbrowser
from googlesearch import *
import os
import math
import time
import sys
import pyttsx3
import speech_recognition as sr
import datetime
import random
import smtplib
import subprocess
from selenium import webdriver
from ecapture import ecapture as ec
import playsound
from gtts import gTTS
import wolframalpha
import ctypes
import pyjokes
import logo
import wmi
import pandas as pd
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth

from atomipy import *

# Set variables from setup.txt
setup = pd.read_csv('F:\\Python\\Mini_project\\setup.txt', sep='=', index_col=0, squeeze=True, header=None)
client_id = setup['client_id']
client_secret = setup['client_secret']
device_name = setup['device_name']
redirect_uri = setup['redirect_uri']
scope = setup['scope']
username = setup['username']

# Connecting to the Spotify account
auth_manager = SpotifyOAuth(
client_id=client_id,
client_secret=client_secret,
redirect_uri=redirect_uri,
scope=scope,
username=username)
spotify = sp.Spotify(auth_manager=auth_manager)

# Selecting device to play from
devices = spotify.devices()
deviceID = None
for d in devices['devices']:
    d['name'] = d['name']
    if d['name'] == device_name:
        deviceID = d['id']
        break


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

            # elif "spotify" in query and "play" in query:
            #     query = query.replace("play", "")
            #     query = query.replace("spotify", "")
            #     print(query)
            #     continue

if __name__ == "__main__":
    logo.atomic_logo()

    try:
        while True:

            speak("Tell me")
            query = takeCommand().lower()


            if query == 0:
                continue

            elif 'exit' in query or 'bye' in query or 'see you later' in query or 'stop' in query:
                speak("As you wish, Anything for you.")
                exit()

            elif "spotify" in query and "play" in query:
                query = query.replace("play","")
                query = query.replace("on spotify","")
                query = query.replace("in spotify","").strip()
                speak(query)

                try:
                    if "album" in query:
                        speak("Playing album on Spotify")
                    elif "artist" in query:
                        speak("Playing artist on Spotify")
                    else:
                        speak("Playing on Spotify")
                        name = query
                        uri = get_track_uri(spotify=spotify, name=name)
                        play_track(spotify=spotify, device_id=deviceID, uri=uri)
                        speak("Enjoy Listening")
                        break

                except InvalidSearchError:
                    speak("Invalid Search Error, Try Again")
                    # break

    except Exception as e:
    	speak("Oh...I think I need my MEDIC, something wrong happened with my code.")
    	exit()

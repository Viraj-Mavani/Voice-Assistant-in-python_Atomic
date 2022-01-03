import wikipedia
import webbrowser
from googlesearch import *
import webbrowser
import os
import subprocess
import math
import time
import sys

query = "retart the pc"

try:
    if "restart" in query and ("pc" in query or "laptop" in query or "device" in query):
        print("Ok , your pc will restart in 10 sec make sure you exit from all applications")
        # subprocess.call(["shutdown", "/r", "/t", "10")
        os.system("shutdown /s /t 10")
except Exception as e:
    print(e)

import wikipedia
import webbrowser
from googlesearch import *
import webbrowser

query = "search sherlock holmes"

if "speak" in query:
    query = query.replace("speak","")
    print(query)

elif ('wikipedia' in query and 'search' in query) or ('wikipedia' in query):
    query = query.replace("in wikipedia", "")
    query = query.replace("wikipedia", "")
    query = query.replace("search", "").strip()
    print(f'Searching {query}')
    results = wikipedia.summary(query, sentences=2)
    print("According to Wikipedia")
    print(results)

elif 'google' in query or 'search' in query:
    query = query.replace("search", "")
    query = query.replace("in google", "")
    query = query.replace("google", "")
    query = query.replace("on google", "").strip()
    print(f"searching {query} in google")
    print("you googled bro!!!!! " + query)
    print("here is your result. Anything else?")

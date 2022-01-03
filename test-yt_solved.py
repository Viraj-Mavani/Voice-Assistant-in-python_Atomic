import wikipedia
import webbrowser

query = "play thoda thoda pyar"

#------------------dont-------------------
#
# if "play" in query:
#     print(f"playing {query} in youtube")
#     api_key = "AIzaSyDHWXEhskRq65bfurRDr18PC8uE6ruMjTU"
#     from apiclient.discovery import build
#     query= query.split("play")
#     print(f"{query}")
#     query = str(query[0: ])
#     print(f"{query}")
#     youtube = build("youtube" , "v3" , developerKey = api_key)
#     print(f"{query}")
#     query = youtube.search().list(q = query ,part="id",type="video",fields="items/id")
#     print(f"{query}")
#     query = query.execute()
#     query = query['items'][0]['id']['videoId']
#     print(query)
#     # webbrowser.open("https://www.youtube.com/watch?v=" + query)
#     # VaT7IYQgyqo


#------------------do-------------------
if "play" in query:
    query = query.replace("play ", "")
    query = query.replace("in youtube", "")
    query = query.replace("on youtube", "").strip()
    print(f"playing {query} in youtube")
    api_key = "AIzaSyDHWXEhskRq65bfurRDr18PC8uE6ruMjTU"
    from apiclient.discovery import build
    # query= query.split("play")
    # query = str(query[0: ])
    youtube = build("youtube" , "v3" , developerKey = api_key)
    print(f"{query}")
    query = youtube.search().list(q = query ,part="id",type="video",fields="items/id")
    print(f"{query}")
    query = query.execute()
    query = query['items'][0]['id']['videoId']
    print(query)
    webbrowser.open("https://www.youtube.com/watch?v=" + query)
    # VaT7IYQgyqo
    # iDQ396yTrC8

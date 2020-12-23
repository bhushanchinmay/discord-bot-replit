############################################
# Using Google API: Custom Search JSON API #
# Programmable Search Engine               #
############################################

import os
from googleapiclient.discovery import build

API_KEY = os.getenv('API_KEY')
SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID')


def search(query):
    # service object for interacting with the API
    service = build("customsearch", "v1", developerKey=API_KEY)

    res = service.cse().list(
        q=query,
        cx=SEARCH_ENGINE_ID,
    ).execute()

    # Handles if no result is found
    try:
        items = res["items"]
        top_five_links = []
        for i in items:
            if (len(top_five_links) < 5):
                top_five_links.append(i["link"])
        print(top_five_links)
        return top_five_links
    except:
        return

from replit import db
import re

searched_list = []

if "search" in db.keys():
    searched_list = searched_list + db["search"]

def update_search_history(query):
  if "search" in db.keys():
    search_history = db["search"]
    search_history.append(query)
    db["search"] = search_history
  else:
    db["search"] = [query]


def retrieve_search(query):
  search_history = db["search"]
  print(search_history)
  r = re.compile("("+query+")")
  return list(filter(r.match, search_history))

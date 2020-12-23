from googlesearch import search

def search_result(query):

    top_five_results = []

    for result in search(query, tld='com', lang="en", stop=5, pause=2):
        top_five_results.append(result)

    return top_five_results
import json
import requests


def get_search(year, mov_format, title):
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    querystring = {"page": "1", "y": year, "r": "json", "type": mov_format, "s": title}
    headers = {
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
        'x-rapidapi-key': "8cededac22msh108d17365db6155p1a4c47jsn63343757047a"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = json.loads(response.text)
    return result

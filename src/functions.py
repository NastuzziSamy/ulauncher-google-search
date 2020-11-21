import json
import urllib.request


GOOGLE_SUGGESTION_URL = 'https://google.com/complete/search?output=firefox&q='


def search_from_google(search):
    req = urllib.request.urlopen(GOOGLE_SUGGESTION_URL + search)
    data = req.read()

    encoding = req.info().get_content_charset('utf-8')

    return json.loads(data.decode(encoding))[1]


print(search_from_google('a'))
import requests
import json
from languages import LANGUAGES

class Translate:
    def __init__(self, text, fromlang, tolang):
        lang = fromlang + "|" + tolang
        response = requests.get(url="https://api.mymemory.translated.net/get?q={}&langpair={}".format(text, lang))
        self.req = json.loads(response.content.decode())
    
    def GetAll(self):
        return self.req
    
    def GetTranslatedText(self):
        return self.req["responseData"]["translatedText"]
    
    def GetMatches(self):
        return self.req["matches"]
    
    def GetFormatedMatches(self):
        words = []
        for i in self.req["matches"]:
            words.append(i["translation"])
        return words
    
    def GetLanguages():
        fromatedLnaguages = []
        for keys, items in LANGUAGES.items():
            fromatedLnaguages.append("{} is for {} language".format(keys,items))
        return fromatedLnaguages


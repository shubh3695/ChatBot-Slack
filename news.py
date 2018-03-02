import requests
import json

'''

@author ssaxena36

'''

class News(object):
    def __init__(self):
        file = open("/home/ssaxena36/Desktop/Hack36Apps/apiKey.txt", "r")
        self.apiKey = (file.read().strip())

    def getNews(self, word):
        articles = requests.get(
            'https://newsapi.org/v2/everything?q='+word+'&apiKey='+self.apiKey).json()
        if articles == None:
            return "No News. :("
        res = ""
        i = 0
        for article in articles['articles']:
            res += 'Title: '+article['title'] + '\n'
            res += 'URL: ' + article['url'] + '\n'
            res += 'Description: '+article['description']+'\n\n'
            i += 1
            if i == 5:
                break
        return res

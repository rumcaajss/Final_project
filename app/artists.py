import requests
import json
from django.shortcuts import render
from django.http import HttpResponse
import re

class ArtistParser:

    API_KEY = '93903103571bcd8ca15d664cbe16d6c9'
    API_URL = 'http://ws.audioscrobbler.com/2.0/'
    def __init__(self, name):
        self.name = name

    def downloadArtists(self):
        parameters = {'method' : 'user.gettopartists', 'user': self.name, 'api_key': ArtistParser.API_KEY, 'format' : 'json'}
        result = requests.get(ArtistParser.API_URL,params=parameters)
        resultdict = json.loads(result.content.decode("utf-8"))
        regx = re.compile('\'name\': u\'(\w*\s?\/?\w*-?\s?\w*\s?\w*)\'')
        artists = regx.findall(str(resultdict))
        return artists
    
class Compare:
    def __init__(self, artists_1, artists_2):
        self.artists_1=artists_1
        self.artists_2=artists_2
    def checkCommon(self):
        commonArtists=[]
        for x in range(0, 20):
            for y in range (0, 20):
                if self.artists_1[x] == self.artists_2[y]:
                    commonArtists.append(self.artists_1[x])
        if commonArtists==[]:
            no_match=["No matches found, sorry"]
            return no_match
        else:
            return commonArtists

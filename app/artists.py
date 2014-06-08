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

    def downloadArtists(name):
        parameters = {'method' : 'user.gettopartists', 'user': name, 'api_key': ArtistParser.API_KEY, 'format' : 'json'}
        result = requests.get(ArtistParser.API_URL,params=parameters)
        resultdict = json.loads(result.content.decode("utf-8"))
        regx = re.compile('\'name\': \'(\w*\s?\/?\w*-?\s?\w*\s?\w*)\'')
        artists = regx.findall(str(resultdict))
        return resultdict.items()

    def downloadPlaycount(name):
        parameters = {'method' : 'user.gettopartists', 'user': name, 'api_key': ArtistParser.API_KEY, 'format' : 'json'}
        result = requests.get(ArtistParser.API_URL,params=parameters)
        resultdict = json.loads(result.content.decode("utf-8"))
        regx = re.compile('\'playcount\': \'(\d*)\',')
        playcount = regx.findall(str(resultdict))
        return playcount

class Compare:
    def checkCommon(artists_1, artists_2):
        commonArtists=[]
        playcountIndex_1=[]
        playcountIndex_2=[]
        return artists_1
        for x in range(0, 50):
             for y in range (0, 50):
                 if artists_1[x] == artists_2[y]:
                      commonArtists.append(artists_1[x])

        return commonArtists

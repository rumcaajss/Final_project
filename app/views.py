from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template import Template, Context, loader, RequestContext
from app.artists import ArtistParser
from app.artists import Compare

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        name1=request.GET.get('name1','rumcajsss')
        #name2=request.GET.get('name2','rumcajsss')
        template=Template("""
<html>
<head>
<title>Comparision of top artists of two given users.</title>
</head>
<body>
<form>
User 1: <input type="text" name="name1"><br>
<input type="submit" value="Submit">
</form>

</body>
</html>
""")
        user1=ArtistParser(name1)
        context1=Context(user1.downloadArtists)
        return HttpResponse(template.render(context1))
        #return HttpResponse(name1)
        #print (ArtistParser.download('rumcajsss'))
        
        
        #return HttpResponse(template.render(context))
        #zmienna = Compare.checkCommon(ArtistParser.downloadArtists('rumcajsss'),
        #return HttpResponse(user1.downloadArtists())
       
# Create your views here.

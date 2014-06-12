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
        name2=request.GET.get('name2','msitake')
        template=Template("""
<html>
    <head>
        <title>Comparision of top artists of two given users.</title>
    </head>
    <body style="background-color:yellow">
        <div style="width:100%;">
            Write names of LastFm users whose top artists you want to compare
        </div>
        <div style="float:left; width:50%;">
            <form>{% csrf_token %}
                User 1: <input type="text" name="name1"><br>
                User 2: <input type="text" name="name2"><br>
                <input type="submit" value="Submit">
            </form>
            {% for artist in artists1 %}
                <h2>
                    {{ artist }}
                </h2>
            {% endfor %}
        </div>
        <div style="float:right; width:50%;">
            {% for artist in artists2 %}
                <h2>
                    {{ artist }}

                </h2>
            {% endfor %}
        </div>

    </body>
</html>
""")
        user1=ArtistParser(name1)
        artists_list_1 = user1.downloadArtists
        test_lista=[43, 42]
        test_lista2=[2,34]
        #artists_list_2 = ArtistParser.downloadArtists(name2)
        context1=Context({"artists1": test_lista, "artists2": test_lista2})
        #conext2=Context({"artists2": artists_list_2})
        return HttpResponse(template.render(context1))
        

   #<link rel="stylesheet" href="stylesheet.css"/>
        
       
       
# Create your views here.

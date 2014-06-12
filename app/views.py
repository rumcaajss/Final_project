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
    <body>
        <div style="width:100%;height: 100%;background-color:#FFA500;">
            <div id="header" style="width:100%;background-color:#FFA500; text-align:center;">
                <h4>Write names of LastFm users whose top artists you want to compare</h4><br>
                <form>
                    User 1: <input type="text" name="name1"><br>
                    User 2: <input type="text" name="name2"><br>
                    <input type="submit" value="Submit">
                </form>
                
                <h3>Common artists of {{ user1 }} and {{ user2 }} taken from Top20</h3>
                {% for artist in common_artists %}
                    <p>
                        {{ artist }}
                    </p>
                {% endfor %}
            </div>
            <div style="background-color:#FFD700;float:left; width:50%;">
                <h4>Artists of {{ user1 }}</h4>
                {% for artist in artists1 %}
                    <p>
                        {{ artist }}
                    </p>
                {% endfor %}
            </div>
            <div style="background-color:#EEEEEE;float:right; width:50%;">
                <h4>Artists of {{ user2 }}</h4>
                {% for artist in artists2 %}
                    <p>
                        {{ artist }}
                    </p>
                {% endfor %}
            </div>
        </div>
    </body>
</html>
""")
        user1=ArtistParser(name1)
        artists_list_1 = user1.downloadArtists()
        user2=ArtistParser(name2)
        artists_list_2 = user2.downloadArtists()
        comparison=Compare(artists_list_1,artists_list_2)
        common=comparison.checkCommon()
        dictionary={"artists1": artists_list_1, "artists2": artists_list_2, "common_artists": common, 'user1': name1, 'user2': name2}
        context1=Context(dictionary)
        return HttpResponse(template.render(context1))

        
       
       
# Create your views here.

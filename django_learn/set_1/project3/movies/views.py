from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

movies_list = {
    # url: co_se_zobrazi
    "harrypotter": "Harry Potter je",
    "mortalcombat": "Mortal combat je...",
    "smrtvdesti": "Smrt v dešti je...",
    "suicidesquad": None,
}

def index(request):
    movies_names = list(movies_list.keys())
    return render(request, "movies/index.html", {
        "movies_names": movies_names
    })



def allmovies_text(request, moviename):
    try:

        #
        # movie_info = movies_list[moviename]
        # nemusíš psát template
        #response_data = render_to_string("movies/movie.html")
        #return HttpResponse(response_data)
        return render(request, "movies/movie.html", {
            "mytext": "Filip Matura",
            "movie_name": moviename,
            "movie_description": movies_list[moviename]
        })

    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
    


def allmovies_number(request, movienumber):
    movies_names_list = list(movies_list.keys())
    
    if movienumber > len(movies_names_list):
        return HttpResponseNotFound("Film nenalezen")
    
    current_movie = movies_names_list[movienumber - 1]
    redirect_url = reverse("movie_url", args=[current_movie])
    return HttpResponseRedirect(redirect_url)
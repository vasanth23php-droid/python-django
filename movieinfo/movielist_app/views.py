from django.shortcuts import render
from movielist_app.models import Movie
from django.http import JsonResponse

def movie_list(request):
    Movies = Movie.objects.all()
    data   = {"Movies" : list(Movies.values())}
    return JsonResponse(data)
def movie_details(request, id):
    movie = Movie.objects.get(id=id)
    data = {
        'name' : movie.name,
        'description' : movie.description,
        'activate' : movie.activate
    }
    return JsonResponse(data)
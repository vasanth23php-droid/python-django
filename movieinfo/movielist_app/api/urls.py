from django.urls import path, include
from movielist_app.api.view import movie_list, movie_details

urlpatterns = [
        path('list/', movie_list, name='Movie-list'),
        path('<int:id>', movie_details, name='Movie-list'),
    ]
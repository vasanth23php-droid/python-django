from django.contrib import admin
from django.urls import path, include
from movielist_app.views import movie_list,movie_details

urlpatterns = [
        path('list/', movie_list, name='Movie-list'),
        path('<int:id>', movie_details, name='Movie-list'),
    ]
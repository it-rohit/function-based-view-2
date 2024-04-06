
from django.urls import path,include
from .views import movie_list_create,movie_update


urlpatterns = [
    
    
    path('create/', movie_list_create, name='create_movie'),
    path('update/<int:pk>/', movie_update, name='movie_update'),
    
]

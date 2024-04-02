from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('movies/', views.movie_list, name='movie_list'),
    path('add_movie/', views.add_movie, name='add_movie'),
    # Add more URLs as needed
    path('movie/edit/<int:movie_id>/', views.edit_movie, name='edit_movie'),
    path('movie/delete/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('rate_movie/<int:movie_id>/', views.rate_movie, name='rate_movie'),
    path('search/', views.movie_search, name='movie_search')
]

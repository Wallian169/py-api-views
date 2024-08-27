from django.urls import path

from cinema.views import (
    movie_list,
    movie_detail,
    GenreList,
    GenreDetail,
)

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("ganres/", GenreList.as_view(), name="genre-list"),
    path("ganres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
]

app_name = "cinema"

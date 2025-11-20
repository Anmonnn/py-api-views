from django.urls import path

from cinema.views import (
    ActorDetail,
    ActorList,
    CinemaHallDetail,
    CinemaHallList,
    GenreDetail,
    GenreList,
    MovieViewSet,
)

movie_list = MovieViewSet.as_view(actions={"get": "list", "post": "create"})
movie_detail = MovieViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinemaHalls/", CinemaHallList.as_view(), name="cinemaHall-list"),
    path("cinemaHalls/<int:pk>/", CinemaHallDetail.as_view(), name="cinemaHall-detail"),
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]

app_name = "cinema"

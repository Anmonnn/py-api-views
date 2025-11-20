from django.urls import include, path
from rest_framework import routers
from cinema.views import (
    ActorDetail,
    ActorList,
    CinemaHallDetail,
    CinemaHallList,
    GenreDetail,
    GenreList,
    MovieViewSet,
)

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinemaHalls/", CinemaHallList.as_view(), name="cinemaHall-list"),
    path("cinemaHalls/<int:pk>/", CinemaHallDetail.as_view(), name="cinemaHall-detail"),
    path("", include(router.urls)),
    # path("movies/", movie_list, name="movie-list"),
    # path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]

app_name = "cinema"

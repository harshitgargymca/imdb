from django.conf.urls import include, url
from django.contrib import admin
from movies.api_movies.views import MovieViewset
from rest_framework import routers

movie_list = MovieViewset.as_view({'get': 'list'})
movie_detail = MovieViewset.as_view({'get': 'retrieve'})
router = routers.DefaultRouter()
router.register(r'movies', MovieViewset,"basename")

urlpatterns = [
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('register.urls')),
    #url(r'^login/', 'register.views.my_view'),
    url(r'^api/v1/movie_list', movie_list),
    url(r'^api/v1/movie_detail', movie_detail),
   
    #url(r'^api/v1/', include(router.urls)),
]

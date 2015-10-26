from django.conf.urls import include, url
from django.contrib import admin
from movies.api_movies.views import MovieViewset
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'movies', MovieViewset,"basename")

urlpatterns = [
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('register.urls')),
    #url(r'^login/', 'register.views.my_view'),

   
    url(r'^api/v1/', include(router.urls)),
]

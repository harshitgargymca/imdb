from django.conf import urls
from django.conf.urls import url
from .views import BaseLoginview, my_view,registerview,profileview,logout_user, indexview, searchview

urlpatterns = [
	url(r'^$', BaseLoginview),
	url(r'login/$',my_view ),
	url(r'register/$', registerview),
	url(r'profile/$', profileview),
	url(r'logout/$', logout_user),
	url(r'index/$', indexview),
	url(r'search/$', searchview),

	]
from django.contrib import admin
from movies.models import Movie, Genre, Director
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Director)

# Register your models here.

from django.db import models


class Director(models.Model):
	""" This model contains the name of the directors"""

	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class Genre(models.Model):
	type_genre = models.CharField(max_length=300)

	def __unicode__(self):
		return self.type_genre

class Movie(models.Model):
	name = models.CharField(max_length=200)
	popularity= models.DecimalField(max_digits=5,decimal_places=2)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)
	imdb_score = models.DecimalField(max_digits=3,decimal_places=1)
	director = models.ForeignKey(Director)
	genre = models.ManyToManyField(Genre)


	def __unicode__(self):
		return self.name
	
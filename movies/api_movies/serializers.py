from rest_framework import serializers 
from movies.models import Movie, Genre, Director

class GenreSerializer(serializers.ModelSerializer):

	class Meta:
		model = Genre
		fields = ('type_genre',)

class DirectorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Director
		fields = ('name',)
import pdb
class MovieSerializer(serializers.ModelSerializer):
	
	genre = serializers.StringRelatedField(many=True)
	director = serializers.StringRelatedField()

	class Meta:
		model = Movie
		fields = ('name', 'popularity','created_at','modified_at',
			'imdb_score','director','genre')
        read_only = ('created_at','modified_at')

        def to_internal_value(self, validated_data):
        	movie_genre_data = validated_data.pop('genre')
        	movie_name = validated_data['name']
        	movie_popularity = validated_data['popularity']
        	movie_imdb_score = validated_data['imdb_score']

   
        	
        	
        	director_data = validated_data.pop('director')
        	print director_data
        	movie_director, movie_director_flag = Director.objects.get_or_create(name = director_data)
        	movie = Movie.objects.create(name = movie_name,popularity=movie_popularity, imdb_score=movie_imdb_score,director=movie_director)
        	for movie_genre in movie_genre_data:
        		genre_object,genre_object_flag = Genre.objects.get_or_create(type_genre=movie_genre)
        		movie.genre.add(genre_object)
         	return movie

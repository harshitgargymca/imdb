from rest_framework import viewsets, permissions
from .serializers import MovieSerializer 
from rest_framework.response import Response
from movies.models import Movie
from rest_framework.renderers import JSONRenderer

class MovieViewset(viewsets.ViewSet):
	
	serializer_class = MovieSerializer

	def list(self,request):
		queryset = Movie.objects.all()
		#queryset = self.get_queryset()
		print "cool"
		serializer_data = self.serializer_class(queryset, many=True)
		return Response(serializer_data.data)

	def create(self,request,*args, **Kwargs):
		#request_data = request.data.copy()
		#import pdb;pdb.set_trace()
		serializer_data = self.serializer_class(data=request.data)
		
		
		if serializer_data.is_valid():

			
			return Response(serializer_data.data)

	def retrieve(self, request, *args):
		x= request.query_params.get('pk')
		print x
		query = Movie.objects.filter(name__icontains = x)
		serializer_data = self.serializer_class(query,many=True)
		return Response(serializer_data.data)














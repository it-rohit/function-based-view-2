from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status




from .. models import  Movie
from . serializer import MovieSerializer


# view movies and post movie
@api_view(['GET','POST'])
def movie_list_create(request):
    if request.method== 'GET':
        movie = Movie.objects.all()
        serializer1= MovieSerializer(movie, many=True)
        return Response(serializer1.data,status=status.HTTP_200_OK)
    
    if request.method== 'POST':
        data1= request.data
        serializer1 = MovieSerializer(data=data1)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data,status=status.HTTP_201_OK)
        else:
            return Response(serializer1.errors)
        
@api_view(['GET','PUT','DELETE'])
def movie_update(request,pk):
    if request.method=='GET':
        try:

            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response ({"msg":"movie not found"},status=status.HTTP_404_NOT_FOUND)


        serializer1=MovieSerializer(movie)
        return Response (serializer1.data,status=status.HTTP_200_OK)
    
    if request.method=='PUT':
        movie = Movie.objects.get(pk=pk)
        data1=request.data
        serializer1 = MovieSerializer(instance=movie,data=data1)
        if serializer1.is_valid():
            serializer1.save()
            return Response (serializer1.data,status=status.HTTP_201_CREATED)
        else:
            return Response (serializer1.errors)
    if request.method=='DELETE':
        movie= Movie.objects.get(pk=pk)
        movie.delete()
        return Response ({"msg":"movie deleted"})




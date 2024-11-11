from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Movies
from .serializers import MoviesSerializers
from rest_framework.response import Response

class MoviesViewSet(viewsets.ViewSet):
    def list(self,req):
        movies= Movies.objects.all()
        serializers=MoviesSerializers(movies, many=True)
        return Response(serializers.data)
        
    def create(self,req):
        serializers=MoviesSerializers(data=req.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED)
        
    def retrieve(self,req,pk=None):
        movie = Movies.objects.get(id=pk)
        serializer=MoviesSerializers(movie)
        return Response(serializer.data)
        
    def update(self,req,pk=None):
        movie= Movies.objects.get(id=pk)
        serializer=MoviesSerializers(instance=movie, data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def destroy(self,req,pk=None):
        movie= Movies.objects.get(id=pk)
        movie.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
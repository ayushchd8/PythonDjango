from .models import Author, Book
from Hello.serializers import AuthorSerializer, BookSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from django.shortcuts import render

# Create your views here.

class ListAuthorAPIView(ListAPIView): #Display Author list  
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CreateAuthorAPIView(CreateAPIView): #Display to Create Author
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ListBookAPIView(ListAPIView):  #Display Book list
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateBookAPIView(CreateAPIView): #Display to Create book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
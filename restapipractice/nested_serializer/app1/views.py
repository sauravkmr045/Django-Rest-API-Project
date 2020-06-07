from django.shortcuts import render
from .models import Author,Book
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class AuthorListView(ListCreateAPIView):

	queryset = Author.objects.all()
	serializer_class = AuthorSerializer


class AuthorView(RetrieveUpdateDestroyAPIView):

	queryset = Author.objects.all()
	serializer_class = AuthorSerializer


class BookListView(ListCreateAPIView):

	queryset = Book.objects.all()
	serializer_class = BookSerializer


class BookView(RetrieveUpdateDestroyAPIView):

	queryset = Book.objects.all()
	serializer_class = BookSerializer
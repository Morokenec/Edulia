from django.shortcuts import render
from rest_framework import generics
from . import serializers
from library.models import Book


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
# Create your views here.

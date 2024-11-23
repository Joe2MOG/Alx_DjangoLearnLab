from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
import rest_framework.generics as generics  # Import generics as a module
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):  # Use generics to extend ListAPIView
    queryset = Book.objects.all()  # Retrieve all Book instances
    serializer_class = BookSerializer  # Use the BookSerializer for serialization

# Add the BookViewSet for handling CRUD operations (new code)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all Book instances
    serializer_class = BookSerializer  # Use the BookSerializer for serialization
    
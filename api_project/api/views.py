from django.shortcuts import render

# Create your views here.
import rest_framework  # Import the entire rest_framework module
from .models import Book
from .serializers import BookSerializer

class BookList(rest_framework.generics.ListAPIView):  # Extend ListAPIView via rest_framework
    queryset = Book.objects.all()  # Retrieve all Book instances
    serializer_class = BookSerializer  # Use the BookSerializer for serialization

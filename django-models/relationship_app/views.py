from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Query to get all books
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Template for the library details page
    context_object_name = 'library'  # Name of the context variable to access the library in the template

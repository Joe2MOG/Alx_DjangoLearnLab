# Import necessary classes and modules
from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView  # Explicit import for DetailView
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

from django.contrib.auth import login  # Import the login function
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in after successful registration
            return redirect('home')  # Redirect to a home page or another page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login view
class MyLoginView(LoginView):
    template_name = 'login.html'

# Logout view
class MyLogoutView(LogoutView):
    template_name = 'logout.html'

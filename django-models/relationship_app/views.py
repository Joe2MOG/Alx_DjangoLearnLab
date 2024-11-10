from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Library  # Make sure this line is exactly as written
from .models import Book
from django.views.generic.detail import DetailView  # Explicit import for DetailView

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Query to get all books
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library  # Ensure Library is correctly assigned
    template_name = 'relationship_app/library_detail.html'  # Template for the library details page
    context_object_name = 'library'  # Name of the context variable to access the library in the template

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

# Custom check function for the Admin role
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)  # This decorator will check for the admin role
def admin_view(request):
    # Your code here for the admin-specific content or page
    return render(request, 'relationship_app/admin_view.html')

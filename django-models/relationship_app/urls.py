from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # Import Django's built-in LoginView and LogoutView
from .views import register  # Import the register view function

urlpatterns = [
    # URL pattern for function-based view to list all books
    path('books/', list_books, name='list_books'),

    # URL pattern for class-based view to display library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # URL pattern for Django's built-in login view
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    # URL pattern for Django's built-in logout view
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    # URL pattern for the registration view
    path('register/', register, name='register'),
]

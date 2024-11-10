from django.urls import path
from .views import list_books, LibraryDetailView  # Import views here

urlpatterns = [
    # URL pattern for function-based view to list all books
    path('books/', list_books, name='list_books'),

    # URL pattern for class-based view to display library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import path
from .views import MyLoginView, MyLogoutView, register  # Import the views for login, logout, and register

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),  # URL pattern for login view
    path('logout/', MyLogoutView.as_view(), name='logout'),  # URL pattern for logout view
    path('register/', register, name='register'),  # URL pattern for registration view
]

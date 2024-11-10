from django.urls import path
from .views import list_books, LibraryDetailView  # Import views here

urlpatterns = [
    # URL pattern for function-based view to list all books
    path('books/', list_books, name='list_books'),

    # URL pattern for class-based view to display library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import path
from .views import MyLoginView, MyLogoutView, register

urlpatterns = [
    # URL for user registration
    path('register/', register, name='register'),

    # URL for user login
    path('login/', MyLoginView.as_view(), name='login'),

    # URL for user logout
    path('logout/', MyLogoutView.as_view(), name='logout'),
]

from django.urls import path
from .views import list_books, LibraryDetailView, MyLoginView, MyLogoutView, register  # Import all views

urlpatterns = [
    # URL pattern for function-based view to list all books
    path('books/', list_books, name='list_books'),

    # URL pattern for class-based view to display library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # URL pattern for login view (class-based view)
    path('login/', MyLoginView.as_view(), name='login'),

    # URL pattern for logout view (class-based view)
    path('logout/', MyLogoutView.as_view(), name='logout'),

    # URL pattern for registration view (function-based view)
    path('register/', register, name='register'),
]

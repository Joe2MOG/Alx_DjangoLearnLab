from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import the entire views module

urlpatterns = [
    # URL pattern for function-based view to list all books
    path('books/', views.list_books, name='list_books'),

    # URL pattern for class-based view to display library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # URL pattern for Django's built-in login view
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    # URL pattern for Django's built-in logout view
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    # URL pattern for the registration view, explicitly using views.register
    path('register/', views.register, name='register'),  # This line contains "views.register"
]

from django.urls import path
from .views import list_books, LibraryDetailView, register  # Import the views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL pattern for the function-based view to list books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL pattern for the class-based view to display library details
    path('register/', register, name='register'),  # URL pattern for user registration
]

from django.urls import path
from .views import admin_view

urlpatterns = [
    # Other paths...
    path('admin-view/', admin_view, name='admin_view'),  # URL pattern for admin view
]

from django.urls import path
from .views import librarian_view

urlpatterns = [
    # Other paths...
    path('librarian-view/', librarian_view, name='librarian_view'),  # URL pattern for librarian view
]

from django.urls import path
from .views import member_view

urlpatterns = [
    # Other paths...
    path('member-view/', member_view, name='member_view'),  # URL pattern for member view
]

from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]

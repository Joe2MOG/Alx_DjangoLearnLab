from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# The router will automatically generate the URLs for CRUD operations
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Keep the old endpoint for listing books
    path('', include(router.urls)),  # Includes all routes for BookViewSet (CRUD operations)
]

from django.contrib import admin

# Register your models here.
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the admin list view
    search_fields = ('title', 'author')  # Enable search functionality by title and author
    list_filter = ('publication_year',)  # Add filter by publication year
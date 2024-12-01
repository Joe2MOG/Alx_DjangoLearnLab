from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(TestCase):
    def setUp(self):
        # Set up test data
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

        # Create sample books
        self.book1 = Book.objects.create(title="Book One", author_name="Author One", publication_year=2000)
        self.book2 = Book.objects.create(title="Book Two", author_name="Author Two", publication_year=2010)

        # Endpoints
        self.books_url = '/api/books/'
        self.book_detail_url = f'/api/books/{self.book1.id}/'

    def test_list_books(self):
        response = self.client.get(self.books_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        data = {
            "title": "Book Three",
            "author_name": "Author Three",
            "publication_year": 2023
        }
        response = self.client.post(self.books_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        data = {
            "title": "Updated Book One",
            "author_name": "Updated Author One",
            "publication_year": 2001
        }
        response = self.client.put(self.book_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")

    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        response = self.client.get(self.books_url, {'title': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_search_books(self):
        response = self.client.get(self.books_url, {'search': 'Author Two'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author_name'], 'Author Two')

    def test_order_books(self):
        response = self.client.get(self.books_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book One')

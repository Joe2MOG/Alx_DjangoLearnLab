# Delete Operation

**Command**:
```python
from bookshelf.models import Book

# Retrieve the Book instance with the title "Nineteen Eighty-Four"
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book instance
book.delete()  # This removes the book from the database
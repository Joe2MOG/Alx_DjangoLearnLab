# Create Operation Documentation

## Command
```python
from bookshelf.models import Book

# Create a Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()  # Save the book instance to the database

# If the creation is successful, you will not see any output,
# but the book "1984" will be added to the database.

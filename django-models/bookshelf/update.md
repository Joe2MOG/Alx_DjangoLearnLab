# Update Operation

**Command**:
```python
from bookshelf.models import Book

# Retrieve the Book instance with the title "1984"
book = Book.objects.get(title="1984")

# Update the title of the book
book.title = "Nineteen Eighty-Four"
book.save()  # Save the changes to the database
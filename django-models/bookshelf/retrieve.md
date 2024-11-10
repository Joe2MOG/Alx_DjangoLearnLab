# Retrieve Operation

**Command**:
```python
from bookshelf.models import Book

# Retrieve the Book instance with the title "1984"
book = Book.objects.get(title="1984")
book  # Display the book instance


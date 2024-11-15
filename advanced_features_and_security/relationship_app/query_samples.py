from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}: {[book.title for book in books]}")
    except Author.DoesNotExist:
        print("Author not found.")

# List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Many-to-Many relationship
        print(f"Books in {library_name} Library: {[book.title for book in books]}")
    except Library.DoesNotExist:
        print("Library not found.")

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # One-to-One relationship
        print(f"Librarian for {library_name} Library: {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print("Library or librarian not found.")

# Test the queries
if __name__ == "__main__":
    get_books_by_author("Author Name")          # Replace with an actual author name
    list_books_in_library("Library Name")       # Replace with an actual library name
    get_librarian_for_library("Library Name")   # Replace with an actual library name

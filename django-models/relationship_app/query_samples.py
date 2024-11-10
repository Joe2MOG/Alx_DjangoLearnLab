from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    return librarian

# Sample queries to test
if __name__ == "__main__":
    author_name = "J.K. Rowling"  # Change this to a valid author name
    library_name = "City Library"  # Change this to a valid library name

    print("Books by author:", books_by_author(author_name))
    print("Books in library:", books_in_library(library_name))
    print("Librarian of library:", librarian_of_library(library_name))

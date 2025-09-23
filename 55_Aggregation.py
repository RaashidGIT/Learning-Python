# Aggregation = Represents a relationship where one object (the "whole")
# contains references to one or more INDEPENDENT objects (the "parts").
#
# Important: In aggregation, the "part" objects (Book) can exist independently
# of the "whole" (Library). For example, a Book can exist without a Library.


# -----------------------------
# Book Class (the PART)
# -----------------------------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# -----------------------------
# Library Class (the WHOLE)
# -----------------------------
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []   # A Library can have many Books

    def add_book(self, book):
        """Add a Book object to the library's collection"""
        self.books.append(book)

    def list_books(self):
        """Return a list of all books in the library"""
        return [f"{book.title} by {book.author}" for book in self.books]


# -----------------------------
# Create a Library
# -----------------------------
library = Library("New York Public Library")

# -----------------------------
# Create some Books (independent objects)
# -----------------------------
book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
book2 = Book("The Hobbit", "J. R. R. Tolkien")
book3 = Book("The Colour of Magic", "Terry Pratchett")

# -----------------------------
# Add books to the Library
# -----------------------------
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# -----------------------------
# Display the Library info
# -----------------------------
print(f"Welcome to {library.name}")
print("Here are the books we have:")

for book in library.list_books():
    print(f"- {book}")

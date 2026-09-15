# Library Management System

class Library:

    # Constructor
    def __init__(self):
        self.books = []

    # Add a book
    def add_book(self, book):
        self.books.append(book)
        print(book, "has been added.")

    # Display all books
    def display_books(self):
        print("\nBooks in Library:")
        for book in self.books:
            print("-", book)

    # Borrow a book
    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "has been borrowed.")
        else:
            print(book, "is not available.")


# Create a library object
library = Library()

# Add books
library.add_book("Python Programming")
library.add_book("The Secret Garden")
library.add_book("Harry Potter")

# Display books
library.display_books()

# Borrow a book
library.borrow_book("Python Programming")

# Display books again
library.display_books()
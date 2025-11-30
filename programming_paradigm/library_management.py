# library_management.py

class Book:
    """A class representing a book with a title, author, and checkout status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # already checked out

    def return_book(self):
        """Mark the book as returned if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # wasn't checked out

    def is_available(self):
        """Return True if the book is available."""
        return not self._is_checked_out


class Library:
    """A library class that manages a collection of books."""

    def __init__(self):
        self._books = []  # private list of books

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return  # operation done
        print(f"Book '{title}' not found in library.")

    def return_book(self, title):
        """Return a checked-out book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return  # operation done
        print(f"Book '{title}' not found in library.")

    def list_available_books(self):
        """Print all books that are not checked out."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")

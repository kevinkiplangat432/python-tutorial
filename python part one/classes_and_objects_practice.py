# Classes and Objects

# Task 1:
# Create a class `Book` with attributes: title, author, and year.

# Task 2:
# Create a method to display book info.

# Task 3:
# Instantiate two Book objects and print their info.

# Task 4:
# Add a method that returns a dictionary representation of a book (you'll use this idea in Flask JSON APIs).

# Flask Prep Connection:
# Flask models and response objects often use classes to represent and serialize data.





#further needed understanding from AI 
# --- Expert-Level OOP Library System --- #

from datetime import date, timedelta

# -----------------------
# CLASS 1: Book
# -----------------------
class Book:
    """Represents a single book in the library."""

    def __init__(self, title, author, total_copies):
        # __init__ runs automatically when you create a new instance
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow(self):
        """Borrow a copy of the book if available."""
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        else:
            return False

    def return_book(self):
        """Return a borrowed copy."""
        if self.available_copies < self.total_copies:
            self.available_copies += 1

    def __str__(self):
        """Readable representation of the book."""
        return f"{self.title} by {self.author} ({self.available_copies}/{self.total_copies} available)"


# -----------------------
# CLASS 2: User
# -----------------------
class User:
    """Represents a library user."""

    def __init__(self, name):
        self.name = name
        self.borrowed_books = {}  # book_title -> due_date

    def borrow_book(self, book: Book):
        """Try to borrow a book from the library."""
        if book.borrow():
            due_date = date.today() + timedelta(days=14)
            self.borrowed_books[book.title] = due_date
            print(f"{self.name} borrowed '{book.title}' (due on {due_date})")
        else:
            print(f"Sorry {self.name}, '{book.title}' is not available right now.")

    def return_book(self, book: Book):
        """Return a borrowed book."""
        if book.title in self.borrowed_books:
            book.return_book()
            del self.borrowed_books[book.title]
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")

    def list_borrowed_books(self):
        """Show all books borrowed by this user."""
        if not self.borrowed_books:
            print(f"{self.name} has not borrowed any books.")
        else:
            print(f"{self.name}'s borrowed books:")
            for title, due_date in self.borrowed_books.items():
                print(f" - {title} (due on {due_date})")


# -----------------------
# CLASS 3: Library
# -----------------------
class Library:
    """Manages books and users in the library."""

    def __init__(self, name):
        self.name = name
        self.books = []   # list of Book instances
        self.users = []   # list of User instances

    def add_book(self, title, author, copies):
        """Add a new book to the library."""
        book = Book(title, author, copies)
        self.books.append(book)
        print(f"Added '{title}' by {author} ({copies} copies)")

    def register_user(self, name):
        """Add a new user to the system."""
        user = User(name)
        self.users.append(user)
        print(f"Registered new user: {name}")
        return user

    def find_book(self, title):
        """Find a book by title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def show_books(self):
        """Display all books in the library."""
        print(f"\n📚 Books in {self.name}:")
        for book in self.books:
            print(" -", book)


# -----------------------
# DEMONSTRATION
# -----------------------
if __name__ == "__main__":
    # Create a library (this is an instance of Library)
    my_library = Library("Campus Central Library")

    # Add some books
    my_library.add_book("1984", "George Orwell", 3)
    my_library.add_book("Atomic Habits", "James Clear", 2)

    # Register users
    kevin = my_library.register_user("Kevin Kiplangat")
    mary = my_library.register_user("Mary Njeri")

    # Borrow books
    book1 = my_library.find_book("1984")
    kevin.borrow_book(book1)
    mary.borrow_book(book1)

    # List borrowed books
    kevin.list_borrowed_books()
    mary.list_borrowed_books()

    # Return a book
    kevin.return_book(book1)
    kevin.list_borrowed_books()

    # Show current library state
    my_library.show_books()

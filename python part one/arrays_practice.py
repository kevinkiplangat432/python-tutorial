# Arrays in Python (using lists and the array module)

# Task 1: Create a list of book titles and print the first and last title
books = ["Atomic Habits", "Deep Work", "The Alchemist", "Rich Dad Poor Dad", "Think and Grow Rich"]
print("Task 1:")
print("First book:", books[0])
print("Last book:", books[-1])


# Task 2: Append a new title and remove one safely
print("\nTask 2:")
books.append("The Subtle Art of Not Giving a F*ck")   # Add a new title
print("After append:", books)

# Remove safely using try/except (to avoid error if book not found)
book_to_remove = "Deep Work"
if book_to_remove in books:
    books.remove(book_to_remove)
    print(f"'{book_to_remove}' removed successfully.")
else:
    print(f"'{book_to_remove}' not found in the list.")

print("Updated list:", books)


# Task 3: Convert list to a set and back to list to remove duplicates
print("\nTask 3:")
books_with_duplicates = ["Atomic Habits", "The Alchemist", "Atomic Habits", "Think and Grow Rich"]
unique_books = list(set(books_with_duplicates))  # removes duplicates automatically
print("Unique books:", unique_books)


# Task 4 (Optional): Use the array module for integers
print("\nTask 4:")
from array import array

# Create an integer array
nums = array('i', [10, 20, 30, 40])

# Access and modify values
print("Original array:", nums.tolist())
nums.append(50)
nums.remove(20)
nums[0] = 5
print("Modified array:", nums.tolist())


# Flask Prep Connection:
# Lists (and sometimes arrays) are often used in Flask routes.
# For example:
# data = fetch_books_from_db()
# titles = [book["title"] for book in data]
# return render_template("books.html", books=titles)

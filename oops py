## ✅ Objective:
Build a basic **Library Management System** with `Book` and `Member` classes. This allows:
- Viewing book info
- Checking book availability
- Borrowing books

---

## 🧠 Changes Made:
- Fixed method names and logic
- Improved method definitions (added `self` where needed)
- Tracked borrowed books
- Allowed searching by multiple authors
- Clear comments explaining every block

---

## ✅ Final Code with Explanations

```python
from Data import book_data, member_data

# -------------------- BOOK CLASS --------------------
class Book:
    def __init__(self, book_id, title, author, is_available):
        """
        Initializes a book with its ID, title, author, and availability status.
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = is_available

    def __str__(self):
        """
        Displays readable information when print(book) is called.
        """
        return f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Available: {self.is_available}"

    def borrow(self):
        """
        Marks the book as borrowed (i.e., not available).
        """
        if self.is_available:
            self.is_available = False
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def make_available(self):
        """
        Marks the book as available again (e.g., when returned).
        """
        if not self.is_available:
            self.is_available = True
            print(f"'{self.title}' is now available.")
        else:
            print(f"'{self.title}' is already available.")

    @staticmethod
    def book_by_id(book_list, book_id):
        """
        Searches for a book in the list by its ID.
        """
        for book in book_list:
            if book.book_id == book_id:
                return book
        return None

    @staticmethod
    def books_by_author(book_list, author):
        """
        Returns a list of all books written by a given author.
        """
        author_books = [book for book in book_list if book.author.lower() == author.lower()]
        if author_books:
            return author_books
        else:
            print("No books found by that author.")
            return []

# -------------------- CREATE BOOK OBJECTS --------------------
book_objects = []
for data in book_data:
    book = Book(data["book_id"], data["title"], data["author"], data["is_available"])
    book_objects.append(book)

# -------------------- MEMBER CLASS --------------------
class Member:
    def __init__(self, member_id, name, email, phone):
        """
        Initializes a library member with personal info and a list to store borrowed books.
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.borrowed_books = []

    def borrow_book(self, book_id):
        """
        Allows the member to borrow a book if available.
        Tracks borrowed books inside the member's list.
        """
        book = Book.book_by_id(book_objects, book_id)
        if book:
            if book.is_available:
                book.borrow()
                self.borrowed_books.append(book)
                print(f"{self.name} has borrowed '{book.title}'.")
            else:
                print(f"Sorry, '{book.title}' is already borrowed.")
        else:
            print("Invalid Book ID. Book not found.")

    def list_borrowed_books(self):
        """
        Prints all the books borrowed by the member.
        """
        if self.borrowed_books:
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print(f" - {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")

# -------------------- SAMPLE USAGE --------------------

# Find and print a book by ID
print("\n📚 Searching book by ID:")
found_book = Book.book_by_id(book_objects, 1)
if found_book:
    print(found_book)
else:
    print("Book with that ID not found.")

# Find and print books by author
print("\n👨‍🏫 Searching books by Author:")
author_books = Book.books_by_author(book_objects, "George Orwell")
for b in author_books:
    print(b)

# Member borrows a book
print("\n🙋 Member borrowing a book:")
member = Member(101, "Alice", "alice@example.com", "1234567890")
member.borrow_book(1)  # Book ID 1

# Check borrowed books
print("\n📖 Member's borrowed books:")
member.list_borrowed_books()
```

---

## 🔍 How It Works:
| Component | Purpose |
|----------|---------|
| **Book class** | Handles book data, search, availability |
| **Member class** | Handles members borrowing and tracking |
| **book_objects** | Stores all created book instances |
| **book_by_id** | Retrieves book by unique ID |
| **books_by_author** | Retrieves all books from an author |
| **borrow_book()** | Lets members borrow a book if available |
| **list_borrowed_books()** | View what books a member borrowed |

---

Library Management System
│
├── Data (imported)
│   ├── book_data
│   └── member_data
│
├── Class: Book
│   ├── __init__(book_id, title, author, is_available)
│   ├── __str__()
│   ├── borrow()                -> Marks book as borrowed
│   ├── make_available()        -> Makes book available again
│   ├── book_by_id(book_list, book_id)         -> Static method to get book by ID
│   └── books_by_author(book_list, author)     -> Static method to get all books by author
│
├── book_objects = []           # List to store all Book instances
│   └── For loop to populate it from book_data
│
├── Class: Member
│   ├── __init__(member_id, name, email, phone)
│   ├── borrow_book(book_id)    -> Member borrows a book by ID
│   └── list_borrowed_books()   -> Shows member's borrowed books
│
└── Sample Usage
    ├── Book.book_by_id()         -> Find book by ID
    ├── Book.books_by_author()    -> Find book(s) by author
    ├── member = Member(...)      -> Create a member
    ├── member.borrow_book()      -> Borrow a book
    └── member.list_borrowed_books() -> Show borrowed books
  

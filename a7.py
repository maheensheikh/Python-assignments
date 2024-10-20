from typing import List, Dict, Optional
import os

# Base User Class
class User:
    def __init__(self, user_id: int, name: str, email: str) -> None:
        self._user_id: int = user_id
        self._name: str = name
        self._email: str = email
    
    def get_user_info(self) -> str:
        return f"ID: {self._user_id}, Name: {self._name}, Email: {self._email}"

# Librarian Class - Inherits from User
class Librarian(User):
    def __init__(self, user_id: int, name: str, email: str) -> None:
        super().__init__(user_id, name, email)

# Member Class - Inherits from User
class Member(User):
    def __init__(self, user_id: int, name: str, email: str) -> None:
        super().__init__(user_id, name, email)
        self._borrowed_books: List[int] = []

    def borrow_book(self, book_id: int, library_manager: 'LibraryManager') -> None:
        if library_manager.borrow_book(self._user_id, book_id):
            self._borrowed_books.append(book_id)

    def return_book(self, book_id: int, library_manager: 'LibraryManager') -> None:
        if library_manager.return_book(self._user_id, book_id):
            self._borrowed_books.remove(book_id)

# Book Class
class Book:
    def __init__(self, book_id: int, title: str, author: str, available: bool = True) -> None:
        self._book_id: int = book_id
        self._title: str = title
        self._author: str = author
        self._available: bool = available

    def get_book_info(self) -> str:
        return f"ID: {self._book_id}, Title: {self._title}, Author: {self._author}, Available: {self._available}"

# LibraryManager Class for managing Books and Users
class LibraryManager:
    books_file: str = "books.txt"
    users_file: str = "users.txt"
    
    def __init__(self) -> None:
        self.books: Dict[int, Book] = {}  # {book_id: Book}
        self.users: Dict[int, User] = {}  # {user_id: User}
        self.load_books()
        self.load_users()
    
    def load_books(self) -> None:
        if not os.path.exists(LibraryManager.books_file):
            return
        
        try:
            with open(LibraryManager.books_file, 'r') as f:
                for line in f:
                    book_id, title, author, available = line.strip().split(',')
                    self.books[int(book_id)] = Book(int(book_id), title, author, available == "True")
        except IOError:
            print("Error reading books file")

    def load_users(self) -> None:
        if not os.path.exists(LibraryManager.users_file):
            return
        
        try:
            with open(LibraryManager.users_file, 'r') as f:
                for line in f:
                    user_id, name, email, role = line.strip().split(',')
                    if role == 'Librarian':
                        self.users[int(user_id)] = Librarian(int(user_id), name, email)
                    elif role == 'Member':
                        self.users[int(user_id)] = Member(int(user_id), name, email)
        except IOError:
            print("Error reading users file")

    def save_books(self) -> None:
        try:
            with open(LibraryManager.books_file, 'w') as f:
                for book in self.books.values():
                    f.write(f"{book._book_id},{book._title},{book._author},{book._available}\n")
        except IOError:
            print("Error writing to books file")

    def save_users(self) -> None:
        try:
            with open(LibraryManager.users_file, 'w') as f:
                for user in self.users.values():
                    role = 'Librarian' if isinstance(user, Librarian) else 'Member'
                    f.write(f"{user._user_id},{user._name},{user._email},{role}\n")
        except IOError:
            print("Error writing to users file")

    # Book Management
    def add_book(self, title: str, author: str) -> None:
        book_id: int = len(self.books) + 1
        self.books[book_id] = Book(book_id, title, author)
        self.save_books()

    def update_book(self, book_id: int, title: Optional[str] = None, author: Optional[str] = None) -> None:
        if book_id in self.books:
            if title:
                self.books[book_id]._title = title
            if author:
                self.books[book_id]._author = author
            self.save_books()
        else:
            print("Book not found")

    def delete_book(self, book_id: int) -> None:
        if book_id in self.books:
            del self.books[book_id]
            self.save_books()
        else:
            print("Book not found")

    # User Management
    def add_user(self, name: str, email: str, role: str) -> None:
        user_id: int = len(self.users) + 1
        if role == "Librarian":
            self.users[user_id] = Librarian(user_id, name, email)
        elif role == "Member":
            self.users[user_id] = Member(user_id, name, email)
        self.save_users()

    # Book Borrowing and Returning
    def borrow_book(self, user_id: int, book_id: int) -> bool:
        if book_id in self.books and self.books[book_id]._available:
            self.books[book_id]._available = False
            self.save_books()
            return True
        print("Book not available")
        return False

    def return_book(self, user_id: int, book_id: int) -> bool:
        if book_id in self.books and not self.books[book_id]._available:
            self.books[book_id]._available = True
            self.save_books()
            return True
        print("Invalid return")
        return False

    # Display books
    def display_books(self) -> None:
        for book in self.books.values():
            print(book.get_book_info())

# Example Usage
library_manager = LibraryManager()

# Adding Users
library_manager.add_user("Alice", "alice@example.com", "Librarian")
library_manager.add_user("Bob", "bob@example.com", "Member")

# Adding Books
library_manager.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library_manager.add_book("1984", "George Orwell")

# Displaying Books
library_manager.display_books()

# Bob borrows a book
member = library_manager.users[2]  # Assuming Bob has user_id 2
member.borrow_book(1, library_manager)  # Bob borrows book_id 1

# Displaying Books after borrowing
library_manager.display_books()

# Bob returns the book
member.return_book(1, library_manager)

# Displaying Books after return
library_manager.display_books()

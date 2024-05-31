"""
Easy Level: Design a Library Management System
Here are the functional requirements:

Book Management:

Add new books to the library.
Update details about a book.
Remove books from the library.
Search for books by various criteria (title, author, genre).
User Management:

Add new users to the system.
Update user information.
Remove users from the system.
Loan Management:

Check out books to a user.
Check in books returned by a user.
Track overdue books and notify users.
Consider these points:

Each book can have multiple copies.
Books can be reserved if all copies are currently checked out.
Users have a limit on how many books they can borrow at once.
"""

import datetime
import uuid
from collections import deque


class Book:

    def __init__(self, title, author, genre):
        self.id = uuid.uuid4()
        self.title = title
        self.author = author
        self.genre = genre
        self.rented_by = None
        self.copies = 1
        self.reservation_queue = deque()

    def __eq__(self, other):
        return (
                self.title == other.title and
                self.author == other.author and
                self.genre == other.genre
        )


class User:

    def __init__(self, name, email):
        self.email = email
        self.name = name
        self.books_rented = {}

    def __eq__(self, other):
        return self.name == other.name


class System:

    def __init__(self):

        self.books = {}
        self.users = {}

    def add_book(self, book: Book):

        if book.id in self.books:
            self.books[book.id].copies += 1
            print(f"book {book.title} added")
        else:
            self.books[book.id] = book
            print(f"copy of book {book.title} added")

    def add_user(self, user: User):

        if user.email in self.users:
            print(f"user with email {user.email} already exists")
        else:
            self.users[user.email] = user
            print(f"user with email {user.email} added")

    def borrow_book(self, user_id, book_id):

        if user_id in self.users and book_id in self.books:
            user = self.users[user_id]
            book = self.books[book_id]

            if len(user.books_rented) < Constants.MAX_BOOKS_PER_USER and book.copies:
                book.copies -= 1
                user.books_rented[book_id] = datetime.datetime.now()
                print(f"user: {user.email} borrowed book {book.title} successfully")

            else:
                print("user has reached borrowing limit or book is unavailable")
        print("either book_id or user_id is not valid")

    def return_book(self, user_id, book_id):

        if user_id in self.users and book_id in self.books:

            user = self.users[user_id]
            if book_id in user.books_rented:
                book = self.books[book_id]
                book.copies += 1
                del user.books_rented[book_id]
                print("book returned successfully")

                if book.reservation_queue:
                    next_user_id = book.reservation_queue.popleft()
                    self.borrow_book(next_user_id, book_id)
                    print("book reserved successfully")

        print("Invalid user_id or book_id")

    def reserve_book(self, user_id, book_id):

        if user_id in self.users and book_id in self.books:

            book = self.books[book_id]

            if book.copies > 0:
                print("book copy available no need to reserve")
            else:
                if user_id not in book.reservation_queue:
                    book.reservation_queue.append(user_id)
                    print("book reserved successfully")
                else:
                    print("cant reserve same book again")

        print("Invalid user_id or book_id")

    def search_books(self, title=None, genre=None, author=None):

        result = []
        for k, v in self.books:

            if v.title == title or v.genre == genre or v.author == author:
                result.append(v)

        return result

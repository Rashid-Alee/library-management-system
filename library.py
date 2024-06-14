# library.py

from book import Book
from member import Member


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' added successfully.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{title}' removed successfully.")
                return
        print(f"Book '{title}' not found.")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print(f"Book '{title}' found.")
                return
        print(f"Book '{title}' not found.")

    def display_all_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("\n--- All Books ---")
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}")
        print("-----------------")

    def register_member(self, name):
        member = Member(name)
        self.members.append(member)
        print(f"Member '{name}' registered successfully.")

    def remove_member(self, name):
        for member in self.members:
            if member.name == name:
                self.members.remove(member)
                print(f"Member '{name}' removed successfully.")
                return
        print(f"Member '{name}' not found.")

    def display_all_members(self):
        if not self.members:
            print("No members in the library.")
            return
        print("\n--- All Members ---")
        for member in self.members:
            print(f"Name: {member.name}")
        print("-------------------")

    def issue_book(self, title, member_name):
        book_found = False
        member_found = False

        for book in self.books:
            if book.title == title:
                book_found = True
                break

        for member in self.members:
            if member.name == member_name:
                member_found = True
                break

        if not book_found:
            print(f"Book '{title}' not found.")
        elif not member_found:
            print(f"Member '{member_name}' not found.")
        else:
            print(f"Book '{title}' issued to member '{member_name}' successfully.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                print(f"Book '{title}' returned successfully.")
                return
        print(f"Book '{title}' not found.")

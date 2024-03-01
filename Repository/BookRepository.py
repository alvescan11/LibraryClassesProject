from Domain.Book import Book
from Validator.Validator import Validator


class BookRepository:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        for book in self.books:
            if book.getId() == book_id:
                self.books.remove(book)
                break

    def update_book(self, book_id, new_title, new_description, new_author):
        for book in self.books:
            if book.getId() == book_id:
                book.setTitle(new_title)
                book.setDescription(new_description)
                book.setAuthor(new_author)
                break

    def get_all_books(self):
        return self.books

    def get_book_by_id(self,id):
        for book in self.get_all_books():
            if book.getId() == id:
                return book
        return None


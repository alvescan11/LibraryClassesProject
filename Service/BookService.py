from Domain.Book import Book
from Repository.BookRepository import BookRepository
from Validator.Validator import Validator


class BookService:
    def __init__(self,bookRepo: BookRepository, validator: Validator):
        self.bookRepo = bookRepo
        self.validator = validator

    def add_book(self,id,title,description,author):
        book = Book(id,title,description,author)
        self.validator.validate_book(book)
        self.bookRepo.add_book(book)

    def delete_book(self,id):
        self.bookRepo.remove_book(id)

    def update_book(self,id,new_title,new_description,new_author):
        self.bookRepo.update_book(id,new_title,new_description,new_author)

    def find_book(self, string):
        list = []
        for book in self.bookRepo.get_all_books():
            if (
                    string in book.getTitle() or
                    string in book.getDescription() or
                    string in book.getAuthor()
            ):
                list.append(book)
        return list

    def unique_id(self,id):
        for book in self.bookRepo.get_all_books():
            if book.getId() == id:
                return True
        return False

    def get_all(self):
        return self.bookRepo.get_all_books()

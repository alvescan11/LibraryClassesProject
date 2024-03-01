from Domain.Book import Book
from Domain.Client import Client



class Validator:
    def validate_book(self,book: Book):
        errors = []
        if book.getTitle() == "":
            errors.append("Title cannot be empty!!!")
        if book.getAuthor() == "":
            errors.append("Author cannot be empty!!!")
        if book.getDescription() == "":
            errors.append("Description cannot be empty cannot be empty!!!")
        if errors:
            raise ValueError(errors)

    def validate_client(self,client: Client):
        errors = []
        if client.getName() == "":
            errors.append("Name cannot be empty!!!")
        if len(client.CNP) != 13:
            errors.append("CNP must have 13 characters!!!")
        if errors:
            raise ValueError(errors)


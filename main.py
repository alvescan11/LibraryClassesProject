from Domain.Book import Book
from Domain.Library import Library
from Repository.BookFileRepository import BookFileRepository
from Repository.BookRepository import BookRepository
from Repository.ClientFileRepository import ClientFileRepository
from Repository.ClientRepository import ClientRepository
from Repository.LibraryFileRepository import LibraryFileRepository
from Repository.LibraryRepository import LibraryRepository
from Service.BookService import BookService
from Service.ClientService import ClientService
from Service.LibraryService import LibraryService
from Tests.Tests import all_tests
from UI.UI import UserInterface
from Validator.Validator import Validator

if __name__ == '__main__':
    all_tests()
    library_repository = LibraryFileRepository("libraries.txt")
    library_service = LibraryService(library_repository)
    client_validator = Validator()
    client_repository = ClientFileRepository("clients.txt")
    client_service = ClientService(client_repository,client_validator)
    book_validator = Validator()
    book_repository = BookFileRepository("books.txt")
    book_service = BookService(book_repository,book_validator)
    ui = UserInterface(book_service,client_service,library_service)
    ui.runMenu()

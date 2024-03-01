from Domain.Book import Book
from Repository.BookRepository import BookRepository
from Service.BookService import BookService
from Validator.Validator import Validator


def testDomain():
    book = Book("1","asd","ddd","fafsa")
    assert book.getId() == "1"
    assert book.getTitle() == "asd"
    assert book.getDescription() == "ddd"
    assert book.getAuthor() == "fafsa"

def testRepo():
    book = Book("1", "asd", "ddd", "fafsa")
    bookRepo = BookRepository()
    lista = bookRepo.get_all_books()
    assert len(lista) == 0
    bookRepo.add_book(book)
    assert len(lista) == 1
    bookRepo.remove_book("1")
    assert len(lista) == 0

def testFindBook():
    book = Book("1", "asd", "ddd", "fafsa")
    book2 = Book("d","ddd","asda",'x')
    val = Validator()
    bookRepo = BookRepository()
    bookRepo.add_book(book)
    bookRepo.add_book(book2)
    bookService = BookService(bookRepo,val)
    found_book = bookService.find_book("x")
    assert len(found_book) == 1
    assert found_book[0] == book2


def all_tests():
    testDomain()
    testRepo()
    testFindBook()
    print("The tests are succesfully passed!!!")
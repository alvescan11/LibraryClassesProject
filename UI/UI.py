import ast

from Domain.Book import Book
from Domain.Client import Client
from Repository.BookRepository import BookRepository
from Repository.ClientRepository import ClientRepository
from Service.BookService import BookService
from Service.ClientService import ClientService
from Service.LibraryService import LibraryService
from Validator.Validator import Validator


class UserInterface:
    def __init__(self,  bookService: BookService,  clientService: ClientService, libraryService: LibraryService):
        self.bookService = bookService
        self.clientService = clientService
        self.libraryService = libraryService


    def main_menu(self):
        print("1. Book menu")
        print("2. Client menu")
        print("3. Library menu")
        print("x. Exit")

    def menu_book(self):
        print("1. Add book")
        print("2. Delete book")
        print("3. Update book")
        print("4. Find book")
        print("a. Show all books")
        print("x. Back to the main menu")

    def menu_client(self):
        print("1. Add client")
        print("2. Delete client")
        print("3. Update client")
        print("a. Show all clients")
        print("x. Back to the main menu")

    def library_menu(self):
        print("1. Add library")
        print("2. Delete library")
        print("3. Update library")
        print("4. Return book to library")
        print("5. Delete in waterfall")
        print("6. Clients with borrowed books")
        print("a. Show all libraries")
        print("x. Exit")

    def show_all(self,entitati):
        if len(entitati) == 0:
            print("Empty!!!")
        else:
            for entitate in entitati:
                print(entitate)

    def ui_add_books(self):
        try:
            id = input("Give the id: ")
            if self.bookService.unique_id(id):
                print("This id already exists!!!")
                return
            title = input("Give the title: ")
            description = input("Give the description: " )
            author = input("Give the author: ")
            self.bookService.add_book(id,title,description,author)
            print("Book added succesfully!!!")
        except Exception as e:
            print(e)

    def ui_add_clients(self):
        try:
            id = input("Give the id: ")
            if self.clientService.unique_id(id):
                print("This client already exists!!!")
                return
            name = input("Give the name of the client: ")
            CNP = input("Give the CNP of the client: ")
            self.clientService.add_client(id,name,CNP)
            print("Client added succesfully!!!")
        except Exception as e:
            print(e)

    def ui_add_library(self):
        try:
            id = input("Give the id: ")
            if self.libraryService.unique_id(id):
                return
            id_client = input("Give the client's id: ")
            if self.clientService.unique_id(id_client) is False:
                print("This client does't exist!!!")
                return
            id_books = input("Give the id of the books you want, separated by , : ")
            rez = []
            lista = id_books.split(",")
            for elem in lista:
                if self.bookService.unique_id(elem):
                    if elem not in rez:
                        rez.append(elem)
                else:
                    print("One of those books does not exist!!!")
            self.libraryService.add_library(id,id_client,rez)
        except Exception as e:
            print(e)

    def ui_delete_book(self):
        try:
            id = input("Give the id of the book you want to delete: ")
            self.bookService.delete_book(id)
            print("Book deleted succesfully!!!")
        except Exception:
            print("Invalid input!!!")

    def ui_delete_client(self):
        try:
            id = input("Give the id of the client you want to delete: ")
            self.clientService.delete_client(id)
            print("Client deleted succesfully!!!")
        except Exception:
            print("Invalid input!!!")

    def ui_delete_library(self):
        try:
            id = input("Give the id of the library you want to delete: ")
            self.libraryService.remove_library(id)
        except Exception:
            print("error")

    def return_book_from_client(self, id_client, id_book):
        client_found = False
        book_found = False
        for library in self.libraryService.get_all():
            if library.getClientId() == id_client:
                client_found = True
                result = []
                for book in library.getBorrowedBooks():
                    if book != id_book:
                        result.append(book)
                    else:
                        book_found = True
                if book_found:
                    self.libraryService.update_library(library.getId(), id_client, result)
                    print("Book returned successfully.")
                else:
                    print("The client does not have this book!!!")
                break
        if not client_found:
            print("This client does not exist!!!")

    def delete_client_cascade(self, id_client):
        if not self.clientService.unique_id(id_client):
            print("This client does not exist!!!")
        else:
            self.clientService.delete_client(id_client)
            self.libraryService.remove_library(id_client)
            print("Client and associated libraries deleted successfully.")

    def ui_update_book(self):
        id = input("Give the id of the book you want to update: ")
        try:
            title = input("Give the new title: ")
            description = input("Give the new description: ")
            author = input("Give the new author: ")
            self.bookService.update_book(id,title,description,author)
            print("Book updated succesfully!!!")
        except Exception as e:
            print(e)

    def ui_update_client(self):
        id = input("Give the id of the client you want to update: ")
        try:
            name = input("Give the new name: ")
            CNP = input("Give the new CNP: ")
            self.clientService.update_client(id,name,CNP)
            print("Client updated succesfuly!!!")
        except Exception as e:
            print(e)

    def ui_update_library(self):
        id = input("Give the id of the library you want to update: ")
        try:
            id_client = input("Give the new client id: ")
            id_book = input("Give the id of the new books, separated with , : ")
            result = id_book.split(",")
            self.libraryService.update_library(id,id_client,result)
        except Exception:
            print("error")

    def ui_find_book(self):
        string = input("Give a key word: ")
        print(self.bookService.find_book(string))

    def ui_find_client(self):
        string = input("Give a key word: ")
        print(self.clientService.find_client(string))

    def ui_client_with_books(self):
        clients_with_books = self.libraryService.clients_with_borrowed_books(self.clientService)
        for client in clients_with_books:
            print(client)

    def runMenu(self):
        while True:
            self.main_menu()
            option = input("Give option: ")
            if option == "1":
                while True:
                    self.menu_book()
                    option = input("Give the option: ")
                    if option == "1":
                        self.ui_add_books()
                    elif option == "2":
                        self.ui_delete_book()
                    elif option == "3":
                        self.ui_update_book()
                    elif option == "4":
                        self.ui_find_book()
                    elif option == "a":
                        self.show_all(self.bookService.get_all())
                    elif option == "x":
                        break
                    else:
                        print("Wrong option!!!")
            elif option == "2":
                while True:
                    self.menu_client()
                    option = input("Give the option: ")
                    if option == "1":
                        self.ui_add_clients()
                    elif option == "2":
                        self.ui_delete_client()
                    elif option == "3":
                        self.ui_update_client()
                    elif option == "4":
                        self.ui_find_client()
                    elif option == "a":
                        self.show_all(self.clientService.get_all())
                    elif option == "x":
                        break
                    else:
                        print("Wrong option!!!")
            elif option == "3":
                while True:
                    self.library_menu()
                    option = input("Give the option: ")
                    if option == "1":
                        self.ui_add_library()
                    elif option == "2":
                        self.ui_delete_library()
                    elif option == "3":
                        self.ui_update_library()
                    elif option == "4":
                        id_client = input("Give the id of the client who wants to return a book: ")
                        id_book = input("Give the id of the book you want to return: ")
                        self.return_book_from_client(id_client,id_book)
                    elif option == "5":
                        id = input("Give the clients id: ")
                        self.delete_client_cascade(id)
                    elif option == "6":
                        self.ui_client_with_books()
                    elif option == "a":
                        self.show_all(self.libraryService.get_all())
                    elif option == "x":
                        break
                    else:
                        print("Wrong option!!!")
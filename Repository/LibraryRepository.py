from Repository.BookRepository import BookRepository
from Repository.ClientRepository import ClientRepository


class LibraryRepository():
    def __init__(self):
        self.libraries = []

    def add_library(self,library):
        self.libraries.append(library)

    def remove_library(self,id):
        for library in self.libraries:
            if library.getId() == id:
                self.libraries.remove(library)
                break

    def update_library(self,id,id_client,borrowed_books):
        for library in self.libraries:
            if library.getId() == id:
                library.setClientId(id_client)
                library.setBorrowedBooks(borrowed_books)
                break

    def get_all_libraries(self):
        return self.libraries

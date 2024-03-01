from Domain.Library import Library
from Repository.ClientRepository import ClientRepository
from Repository.LibraryFileRepository import LibraryFileRepository
from Repository.LibraryRepository import LibraryRepository


class LibraryService():
    def __init__(self, libraryRepo: LibraryRepository):
        self.libraryRepo = libraryRepo

    def add_library(self,id,id_client,borrowed_books):
        library = Library(id,id_client,borrowed_books)
        self.libraryRepo.add_library(library)

    def remove_library(self, id):
        self.libraryRepo.remove_library(id)

    def update_library(self,id,id_client,borrowed_books):
        self.libraryRepo.update_library(id,id_client,borrowed_books)

    def get_all(self):
        return self.libraryRepo.get_all_libraries()

    def find_by_id(self,id):
        for library in self.libraryRepo.get_all_libraries():
            if library.getId() == id:
                return library

    def clients_with_borrowed_books(self):
        list = []
        for library in self.get_all():
            list.append(library.getClientId())
        return list

    def unique_id(self,id):
        for library in self.libraryRepo.get_all_libraries():
            if library.getId() == id:
                return True
        return False
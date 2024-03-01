from Domain.Library import Library
from Repository.LibraryRepository import LibraryRepository


class LibraryFileRepository(LibraryRepository):
    def __init__(self,file_name):
        super().__init__()
        self.file_name = file_name
        self.read_from_file()

    def add_library(self,library):
        super().add_library(library)
        self.write_to_file()

    def remove_library(self,id):
        super().remove_library(id)
        self.write_to_file()

    def update_library(self,id,id_client,borrowed_books):
        super().update_library(id,id_client,borrowed_books)
        self.write_to_file()

    def read_from_file(self):
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        id, id_client, borrowed_books = line.split("/")
                        library = Library(id,id_client,borrowed_books)
                        super().add_library(library)
        except FileNotFoundError:
            print(f"File {self.file_name} not found. Creating a new file.")

    def write_to_file(self):
        try:
            with open(self.file_name, "w") as file:
                for library in self.get_all_libraries():
                    id = library.getId()
                    id_client = library.getClientId()
                    borrowed_books = library.getBorrowedBooks()
                    line = f"{id}/{id_client}/{borrowed_books}\n"
                    file.write(line)
        except IOError as e:
            print(f"Error writing to {self.file_name}: {e}")

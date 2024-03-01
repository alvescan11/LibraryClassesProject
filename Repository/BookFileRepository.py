from Domain.Book import Book
from Repository.BookRepository import BookRepository

class BookFileRepository(BookRepository):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.read_from_file()

    def add_book(self, book):
        super().add_book(book)
        self.write_to_file()

    def remove_book(self, book_id):
        super().remove_book(book_id)
        self.write_to_file()

    def update_book(self, book_id, new_title, new_description, new_author):
        super().update_book(book_id, new_title, new_description, new_author)
        self.write_to_file()

    def read_from_file(self):
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        id, title, description, author = line.split(",")
                        book = Book(id, title, description, author)
                        super().add_book(book)
        except FileNotFoundError:
            print(f"File {self.file_name} not found. Creating a new file.")

    def write_to_file(self):
        try:
            with open(self.file_name, "w") as file:
                for book in self.get_all_books():
                    id = book.getId()
                    title = book.getTitle()
                    description = book.getDescription()
                    author = book.getAuthor()
                    line = f"{id},{title},{description},{author}\n"
                    file.write(line)
        except IOError as e:
            print(f"Error writing to {self.file_name}: {e}")

class Library:
    def __init__(self,id,client_id,borrowed_books):
        self.id = id
        self.client_id = client_id
        self.borrowed_books = borrowed_books

    def getId(self):
        return self.id

    def getClientId(self):
        return self.client_id

    def getBorrowedBooks(self):
        return self.borrowed_books

    def setClientId(self,client_id):
        self.client_id = client_id

    def setBorrowedBooks(self,borrowed_books):
        self.borrowed_books = borrowed_books

    def __str__(self):
        return f"Library Id: {self.id}, Client Id: {self.client_id}, Borrowed books: {self.borrowed_books} "
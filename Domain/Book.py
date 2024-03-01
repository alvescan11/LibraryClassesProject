from datetime import datetime, timedelta


class Book:
    def __init__(self,id,title,description,author):
        self.id = id
        self.title = title
        self.description = description
        self.author = author

    def getId(self):
        return self.id

    def setId(self,id):
        self.id = id

    def getTitle(self):
        return self.title

    def setTitle(self,title):
        self.title = title

    def getDescription(self):
        return self.description

    def setDescription(self,description):
        self.description = description

    def getAuthor(self):
        return self.author

    def setAuthor(self,author):
        self.author = author

    def getStatus(self):
        return self.status

    def setStatus(self,status):
        self.status = status



    def __repr__(self):
        return f"Id: {self.id}, Title: {self.title}, Description: {self.description}, Author: {self.author}"
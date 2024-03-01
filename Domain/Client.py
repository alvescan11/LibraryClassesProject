class Client:
    def __init__(self,id ,name, CNP):
        self.id = id
        self.name = name
        self.CNP = CNP

    def getId(self):
        return self.id

    def setId(self,id):
        self.id = id

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getCNP(self):
        return self.CNP

    def setCNP(self,CNP):
        self.CNP = CNP

    def __repr__(self):
        return f"Id: {self.getId()}, Name: {self.getName()}, CNP: {self.getCNP()}"
from Domain.Client import Client
from Repository.ClientRepository import ClientRepository
from Validator.Validator import Validator


class ClientService:
    def __init__(self, clientRepo: ClientRepository, validator: Validator):
        self.clientRepo = clientRepo
        self.validator = validator

    def add_client(self,id,name,CNP):
        client = Client(id,name,CNP)
        self.validator.validate_client(client)
        self.clientRepo.add_client(client)

    def delete_client(self,id):
        self.clientRepo.delete_client(id)

    def update_client(self,id,name,CNP):
        self.clientRepo.update_client(id,name,CNP)

    def find_client(self,string):
        lista  = []
        for client in self.clientRepo.get_all_clients():
            if (string in client.getName() or
                string in client.getCNP()):
                lista.append(client)
        return lista

    def unique_id(self,id):
        for client in self.clientRepo.get_all_clients():
            if client.getId() == id:
                return True
        return False

    def get_all(self):
        return self.clientRepo.get_all_clients()
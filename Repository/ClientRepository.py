
from Validator.Validator import Validator

class ClientRepository:
    def __init__(self):
        self.clients = []

    def add_client(self,client):
        self.clients.append(client)

    def delete_client(self,id):
        for client in self.clients:
            if client.getId() == id:
                self.clients.remove(client)
                break

    def update_client(self,id, new_name, new_cnp):
        for client in self.clients:
            if client.getId() == id:
                client.setName(new_name)
                client.setCNP(new_cnp)
                break

    def get_all_clients(self):
        return self.clients

    def get_client_by_id(self,id):
        for client in self.get_all_clients():
            if client.getId() == id:
                return client
        return None
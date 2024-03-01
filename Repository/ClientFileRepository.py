from Domain.Client import Client
from Repository.ClientRepository import ClientRepository


class ClientFileRepository(ClientRepository):
    def __init__(self,file_name):
        super().__init__()
        self.file_name = file_name
        self.read_from_file()

    def add_client(self,client):
        super().add_client(client)
        self.write_to_file()

    def delete_client(self,id):
        super().delete_client(id)
        self.write_to_file()

    def update_client(self,id,name,CNP):
        super().update_client(id,name,CNP)
        self.write_to_file()

    def read_from_file(self):
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        id, name, CNP = line.split(",")
                        client = Client(id,name,CNP)
                        super().add_client(client)
        except FileNotFoundError:
            print(f"File {self.file_name} not found. Creating a new file.")

    def write_to_file(self):
        try:
            with open(self.file_name, "w") as file:
                for client in self.get_all_clients():
                    id = client.getId()
                    name = client.getName()
                    CNP = client.getCNP()
                    line = f"{id},{name},{CNP}\n"
                    file.write(line)
        except IOError as e:
            print(f"Error writing to {self.file_name}: {e}")
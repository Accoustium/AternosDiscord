from python_aternos import Client


class Aternos(Client):
    def __init__(self, username: str, password: str):
        super().__init__()
        self.login(username, password)
        self.servers = self.account.list_servers()

    def get_server(self, server_number: int):
        return self.servers[server_number - 1]

    def start_server(self, server_number: int):
        server = self.get_server(server_number)
        if server:
            server.start()
            return f"Server '{server.address}' started."
        return f"Server '{server.address}' not found."

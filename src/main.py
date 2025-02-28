from python_aternos import Client
from dotenv import load_dotenv
from os import getenv

atclient = Client()
load_dotenv("./src/.env")

# Log in
atclient.login(getenv("USERNAME"), getenv("PASSWORD"))
aternos = atclient.account

servers = aternos.list_servers()

print(servers[0].status)
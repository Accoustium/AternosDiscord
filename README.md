# AternosDiscord

This is a Discord Bot that allows you to start and get the status of an Aternos Minecraft server.

Installation Requirements
---
Before installing and setting up the Bot, you will need somewhere to run it.  This can be on your local PC, or a server that does not go down.  You will also need to install Python 3.11, instructions can be found at [Python.org](https://www.python.org/downloads/).  If you are going to be running this on your local PC, and it is a Windows PC, you will need to install [Git](https://git-scm.com/downloads/win).

Installing the Code
---
Getting the code is as simple as using Git.  You must use the clone command in the terminal, which is as follows `git clone https://github.com/Accoustium/AternosDiscord.git`.  This command will create a folder called AternosDiscord, and install all the code inside.

Discord Setup
---
[Discord Bot Setup](https://discord.com/developers/docs/quick-start/getting-started)

Python Setup
---
Setting up the Python code is fairly simple after you have the code.  Navigate to the `AternosDiscord` folder, and use the following command(s):
### Windows
```bash
python -m pip install poetry
python -m poetry install
```

### Linux/Mac
```bash
pip3 install poetry
python3 -m poetry install
```

After setting up the Poetry environment, need to create a new file in the `src` directory.  The file will be called `.env`.

.env Template:
```text
USERNAME = "" # Aternos Username (Can be Bot with limited Access -- Preferred)
PASSWORD = "" # Aternos Password
DISCORD_TOKEN = "" # Discord Bot Token
DISCORD_GUILD_ID = "" # Discord Server ID
DISCORD_CHANNEL_ID = "" # Discord Channel ID
```

Running the Code
---
To start the Bot, you will just need to navigate inside the `AternosDiscord` folder and run the following command:
### Windows
```bash
python -m pip install -e .
python -m AternosDiscord
```

### Linux/Mac
```bash
python -m pip install -e .
python3 -m AternosDiscord
```

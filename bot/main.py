from bot import Bot
import discord
import os
from datetime import datetime

def main():
    intents = discord.Intents.default()
    intents.message_content = True 
    client = Bot(intents=intents)

    client.run(os.environ['TOKEN'])

if __name__ == '__main__':
    main()
from bot import Bot
import discord
import os

if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True 
    client = Bot(intents=intents)

    client.run(os.environ['TOKEN'])
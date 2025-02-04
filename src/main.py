import discord
from discord.ext import commands, tasks
from discord import app_commands
import os
from datetime import timedelta,datetime
import threading
import sqlite3


class BotClient(discord.Client):

    async def on_ready(self):
        self.tree = app_commands.CommandTree(self)

        self.messages = []
        await self.tree.sync()

    #log取得
    async def on_message(self,msg):
        if msg.author.bot:
            return

        a = False

        for i in range(len(self.messages)):
            if self.messages[i][0] == msg.author.name:
                now = datetime.now()
                self.messages[i][1].append(msg.content)
                self.messages[i][2].append(now)
                a = True

        if a == False:
            msg_list = []
            msg_list.append(msg.content)

            now = datetime.now()
            date_list = []
            date_list.append(now)

            self.messages.append((msg.author.name, msg_list,date_list))

        print(self.messages)

if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True 
    client = BotClient(intents=intents)

    client.run(os.environ['TOKEN'])
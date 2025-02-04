import discord
from discord.ext import commands, tasks
from discord import app_commands
from datetime import datetime
import sqlite3
from commands import Commands

class Bot(commands.Bot):

    def __init__(self, intents):
        # Botの初期化。プレフィックスはスラッシュコマンドを使っているので不要
        super().__init__(command_prefix="!", intents=intents)


    async def on_ready(self):
        self.messages = []

    async def setup_hook(self):
        await self.add_cog(Commands(self))

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
        print('test')
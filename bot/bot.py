import discord
from discord.ext import commands, tasks
from discord import app_commands
from datetime import datetime
from commands import Commands
from db.sql import DataBase
from datetime import timedelta

class Bot(commands.Bot):

    def __init__(self, intents):
        # Botの初期化。プレフィックスはスラッシュコマンドを使っているので不要
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        self.db = DataBase()
        self.messages = []

    async def setup_hook(self):
        await self.add_cog(Commands(self))

    #messages = [
    #   (author_name1,msg_list,datetime_list),
    #   (author_name2,msg_list,datetime_list),
    #   (author_name3,msg_list,datetime_list),
    #]
    async def on_message(self,msg):
        if msg.author.bot:
            return

        a = False

        for i in range(len(self.messages)):
            if self.messages[i][0] == msg.author.name:
                now = datetime.now()
                self.messages[i][1].append(msg)
                self.messages[i][2].append(now)
                a = True

        if a == False:
            msg_list = []
            msg_list.append(msg)

            now = datetime.now()
            date_list = []
            date_list.append(now)

            self.messages.append((msg.author.name, msg_list,date_list))

        for i in range(len(self.messages)):
            msg_list = self.messages[i][1]
            date_list = self.messages[i][2]
            
            try: 
                time_diff = date_list[-1] - date_list[-5]
                seconds = time_diff.total_seconds()
                if seconds <= 4:
                    channel = msg_list[-1].channel
                    print(f'チャンネル「{channel}」で「{msg_list[-1].author}」によるスパムが発生')
                    
                    await msg_list[-1].author.timeout(timedelta(seconds=300))

            except IndexError as err:
                print(err)
import discord
from discord.ext import commands, tasks
from discord import app_commands
import os
from datetime import timedelta,datetime
import threading

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()


@bot.tree.command(name="rules",description="鯖の制限を決めるbot",guild=discord.Object(id=1301092560844099624))
async def decide_rules(interaction: discord.Interaction, max_pitch:int,link:bool,description:str):
    channel = discord.utils.get(interaction.guild.channels, name='server-rules')
    if channel:
        await interaction.response.send_message('successful!')
        channel.send(f'# !この鯖では{max_pitch}回連投するとタイムアウトされます\n{'# !リンク送信は有効です'if link else '# リンク送信は無効です'}')

        channel.send()
    else:
        await interaction.response.send_message("'server_rules' channel not found.")

#messages = [
#   ( msgauthor1,msg_list,date_list )
#   ( msgauthor2,msg_list,date_list )
#   ( msgauthor3,msg_list,date_list )
#]

messages = []

#log取得
@bot.event
async def on_message(msg):
    if msg.author.bot:
        return

    a = False

    for i in range(len(messages)):
        if messages[i][0] == msg.author.name:
            now = datetime.now()
            messages[i][1].append(msg.content)
            messages[i][2].append(now)
            a = True

    if a == False:
        msg_list = []
        msg_list.append(msg.content)

        now = datetime.now()
        date_list = []
        date_list.append(now)

        messages.append((msg.author.name, msg_list,date_list))

    print(messages)

    await bot.process_commands(msg)

bot.run(os.environ['TOKEN'])
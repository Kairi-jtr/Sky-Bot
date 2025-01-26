import discord
from discord.ext import commands, tasks
from discord import app_commands
import asyncio
import re
import os

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='/', intents=intents)

message_authors = []

@bot.tree.command(name="hello",description="テストコマンドです。")
async def test_command(interaction: discord.Interaction):
    await interaction.response.send_message("てすと！",ephemeral=True)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    arashi_check.start()

    await bot.tree.sync()

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    #メッセージ保存
    text = message.content
    author = message.author
    author_name = author.name

    a = False

    for i in range(len(message_authors)):
        if message_authors[i][0] == author_name:
            message_authors[i][1].append(message)
            a = True
            break

    if a == False:
        list = []
        list.append(message)
        message_authors.append((author_name,list))

    await bot.process_commands(message)

@tasks.loop(seconds=5)
async def arashi_check():
    text = []
    for i in range(len(message_authors)):
        msg_list = message_authors[i][1]
        if len(msg_list) > 5:
            for k in msg_list:
                await k.delete()

            channnel = bot.get_channel(1332697911502438412)
            await channnel.send("スパムを削除しました。")

    message_authors.clear()
    print('reset')

bot.run(os.environ['TOKEN'])
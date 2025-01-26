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

    task.start()

    await bot.tree.sync()

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    #メッセージ保存
    text = message.content
    author = message.author
    author_name = author.name
    author_id = author.id

    for auth0r, vector in message_authors:
        if auth0r == author_name:
            vector.append
            break
        else:
            vector.append(text)
            message_authors.append((author_name,vector))

    await bot.process_commands(message)

@tasks.loop(seconds=10)
async def task():   

    message_authors.clear()
    print('test')

bot.run(os.environ['TOKEN'])
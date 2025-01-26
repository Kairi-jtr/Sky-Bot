import discord
from discord.ext import commands, tasks
from discord import app_commands
import asyncio
import re

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='/', intents=intents)

message_authors = []

@bot.tree.command(name="test",description="テストコマンドです。")
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
    
    messages = []

    #メッセージ保存
    author = message.author
    author_name = author.name
    author_id = author.id

    for author, vector in message_authors:
        if author == author_name:
            author

    messages.append((author_name,message.content,message))

    await bot.process_commands(message)

@bot.tree.command(name='hello', description='てすと用') 
@app_commands.guilds(1301092560844099624)
async def test(interaction: discord.Interaction,user: discord.User): 
  await interaction.response.send_message('てすと!')

@tasks.loop(seconds=10)
async def task():   
    print('test')

# botを実行
bot.run('')
import discord
from discord.ext import commands, tasks
from discord import app_commands
import os
from datetime import timedelta

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='/', intents=intents)

message_authors = []

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    arashi_check.start()

    await bot.tree.sync()

@bot.tree.command(name="rules",description="鯖の制限を決めるbot")
async def decide_rules(interaction: discord.Interaction, text:str):
    channel = discord.utils.get(interaction.guild.channels, name='server-rules')
    if channel:
        print('t')
    else:
        await interaction.response.send_message('server_rulesが見つかりませんでした。チャンネルを作成してください。')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    #メッセージ保存
    author = message.author
    author_name = author.name

    if message.content in 'discord.gg':
        timeout_duration = timedelta(minutes=5)
        await message.author.timeout(timeout_duration)
        message.delete()  

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

@tasks.loop(seconds=3)
async def arashi_check():
    for i in range(len(message_authors)):
        msg_list = message_authors[i][1]
        if len(msg_list) > 3:
            #timeout_duration = timedelta(minutes=5)
            #await msg_list[0].author.timeout(timeout_duration)

            for msg in msg_list:
                await msg.delete()            

            print('スパムを削除')

    message_authors.clear()
    print('reset')

bot.run(os.environ['TOKEN'])
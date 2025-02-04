import discord
from discord.ext import commands, tasks
from discord import app_commands
import os
from datetime import timedelta
import threading

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='/', intents=intents)

message_authors = []

@bot.event
async def on_ready():
    arashi_check.start()

    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"同期されたコマンド数: {len(synced)}")
    except Exception as e:
        print(f"同期エラー: {e}")


@bot.tree.command(name="rules",description="鯖の制限を決めるbot",guild=discord.Object(id=1301092560844099624))
async def decide_rules(interaction: discord.Interaction, max_pitch:int,link:bool,description:str):
    channel = discord.utils.get(interaction.guild.channels, name='server-rules')
    if channel:
        await interaction.response.send_message('successful!')
        channel.send(f'# !この鯖では{max_pitch}回連投するとタイムアウトされます\n{'# !リンク送信は有効です'if link else '# リンク送信は無効です'}')

        channel.send()
    else:
        await interaction.response.send_message("'server_rules' channel not found.")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    #メッセージ保存
    author = message.author
    author_name = author.name

    if message.content in 'discord.gg':
        try:
            timeout_duration = timedelta(minutes=5)
            await message.author.timeout(timeout_duration)
        except discord.errors.Forbidden:
            print('許可がない')
        
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
            try:
                timeout_duration = timedelta(minutes=5)
                await msg_list[0].author.timeout(timeout_duration)
            except discord.errors.Forbidden:
                print('許可がない')

        for msg in msg_list:
            await msg.delete()

        print('スパムを削除')

    message_authors.clear()
    print('reset')


bot.run(os.environ['TOKEN'])
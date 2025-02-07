import discord
from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('login')

    @discord.app_commands.command(name="hello", description="Say hello to the bot!")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello! 👋")

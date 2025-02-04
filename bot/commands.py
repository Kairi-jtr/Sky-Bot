import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("test!")

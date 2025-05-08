import discord
from discord.ext import commands

class Ping(commands.Cog):  # Ensure the class derives from commands.Cog
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name=ping)  # This decorator now belongs to the method inside the class
    async def ping(self, ctx):
        """Responds with 'Pong!' and shows the bot's latency."""
        latency = round(self.bot.latency * 1000)  # Latency in milliseconds
        await ctx.send(f"Pong! 🏓 Latency: {latency}ms")

async def setup(bot):
    await bot.add_cog(Ping(bot))  # Add the cog to the bot

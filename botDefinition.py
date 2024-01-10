import discord
from discord.ext import commands
from discord.ext import tasks

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
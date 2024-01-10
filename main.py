import discord
from discord.ext import commands
from discord.ext import tasks
import os
from keepalive import keep_alive 
import commands
from commands import bot

keep_alive()
bot.run(os.getenv('TOKEN'))
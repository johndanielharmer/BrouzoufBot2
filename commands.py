import discord
from discord.ext import commands
from discord.ext import tasks
import botDefinition
from botDefinition import bot

@bot.command(name='speak')
async def postBrouzouf(ctx):
	await ctx.send("Testing")


#THIS EVEN SWALLOWS ALL OTHER EVENTS
#@bot.event
#async def on_message(message):
	#if message.author == bot.user:
		#return

	#if message.content.startswith('$hello'):
		#await message.channel.send('Hello!')
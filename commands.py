import discord
from discord.ext import commands
from discord.ext import tasks
import botDefinition
from botDefinition import bot

@bot.command(name='speak')
async def postBrouzouf(ctx):
	await ctx.send("Testing")

@bot.command(name='persuade')
async def persuade(ctx):
	await ctx.send(
		"https://media1.tenor.com/images/9ff91e34667383b6a6a3ac459b0a3a28/tenor.gif?itemid=15162627"
	)

@bot.command(name='troops')
async def troops(ctx):
	await ctx.send("https://i.imgur.com/IMgXpMm.png")

@bot.command(name='phantom', help='Young Danny Fenton, he was just 14')
async def phantom(ctx):
	await ctx.send("https://i.imgur.com/bkNPbZU.mp4")

@bot.command(name='shocked')
async def shocked(ctx):
	await ctx.send("https://tenor.com/view/shocked-gif-5787388")

@bot.command(name='doit')
async def doit(ctx):
	await ctx.send(
		"https://media1.tenor.com/images/9ff91e34667383b6a6a3ac459b0a3a28/tenor.gif?itemid=15162627"
	)

@bot.command(name='car', help='WHO DO THEY THINK THEY ARE')
async def bwsc(ctx):
	await ctx.send("https://www.youtube.com/watch?v=HpE6ZNo1Duk")

@bot.command(name='ork', help='WAAAAAAAAAAAGH')
async def waagh(ctx):
	await ctx.send("https://www.youtube.com/watch?v=whxcq4I0kAo")

@bot.command(name='jesus', help='I HAVE NO SON')
async def barmitzvah(ctx):
	await ctx.send("https://i.imgur.com/NCWxdA3.png")

@bot.command(name='shutup', help='Bender honey, we love you.')
async def bender(ctx):
	await ctx.send(
		"https://media.tenor.com/images/73b90c45ac3fcbe093c782e28d8ccc06/tenor.gif"
	)

@bot.command(name='bruce',
			 help='The invisible hand of the free market gets me off')
async def bruce(ctx):
	await ctx.send(
"https://cdn.discordapp.com/attachments/473829882858700814/884900693901717605/117127843_1151882928511651_1572153833735867530_n_1.gif"
	)

#THIS EVEN SWALLOWS ALL OTHER EVENTS
#@bot.event
#async def on_message(message):
	#if message.author == bot.user:
		#return

	#if message.content.startswith('$hello'):
		#await message.channel.send('Hello!')
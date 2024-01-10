import discord
from discord.ext import commands
from discord.ext import tasks

import random

def roll(ctx, dice_to_roll: str):

	number_of_dice, number_of_sides = dice_to_roll.split("d")
	number_of_dice = int(number_of_dice)
	number_of_sides = int(number_of_sides)

	if number_of_dice <= 0:
	  #await ctx.send("Needs at least 1 die.")
	  return("Needs at least 1 die.")

	if number_of_sides <= 0:
	  #await ctx.send("Dice needs to have at least 1 side.")
	  return("Dice needs to have at least 1 side.")

	dice = [
		str(random.choice(range(1, number_of_sides + 1)))
		for _ in range(number_of_dice)
	]

	totalList = [eval(i) for i in dice]
	total = str(sum(totalList))
	print(total)
	
	return (', '.join(dice) + ", Total = " + total)

def rolldroplow(ctx, dice_to_roll: str, number_to_drop: int):
	number_of_dice, number_of_sides = dice_to_roll.split("d")
	number_of_dice = int(number_of_dice)
	number_of_sides = int(number_of_sides)
	
	if number_of_dice <= 1:
	  #await ctx.send("Needs at least 2 dice.")
	  return("Needs at least 2 dice.")
	
	if number_to_drop >= number_of_dice:
	  #await ctx.send("You can't drop all the dice!")
	  return("You can't drop all the dice!")
	
	if number_of_sides <= 0:
	  #await ctx.send("Dice needs to have at least 1 side.")
	  return("Needs at least 2 dice.")
	
	dice = [
		str(random.choice(range(1, number_of_sides + 1)))
		for _ in range(number_of_dice)
	]

	dropped = 0
	output = ""
	total = 0
	for i in range(number_of_dice):
		if dice[i] == min(dice) and dropped == 0:
			output = output + "~~" + str(dice[i]) + "~~, "
			dropped = 1
		else:
			output = output + "**" + str(dice[i]) + "**, "
			total = total + int(dice[i])
	output = output + "Total = **" + str(total) + "**"
	return (output)
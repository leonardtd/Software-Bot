import discord 
from discord.ext import commands

client = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
	print("Bot is ready!")

@client.command()
async def drive(ctx):
	await ctx.send("Link del drive:\nhttps://drive.google.com/drive/u/1/folders/1RrIDBAPGEAoN-xOjZcaF8YAwr2nc0lZl")

@client.command()
async def horas(ctx):
	await ctx.send("Horas de trabajo:\nhttps://docs.google.com/spreadsheets/d/13j8lxdUCMzTudtC3HGGWtAoeJ6iOhrUHH2DQiwYrKLU/edit?usp=sharing")

client.run("ODMxNTU0OTE2MTgyMzkyODQ2.YHW73Q.DPwFchd_AIzrzoznpULT7CGp1lc")
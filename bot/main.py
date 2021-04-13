import discord 
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix="?")
token = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
	print("Bot is ready!")

@client.command()
async def drive(ctx):
	await ctx.send("Link del drive:\nhttps://drive.google.com/drive/u/1/folders/1RrIDBAPGEAoN-xOjZcaF8YAwr2nc0lZl")

@client.command()
async def horas(ctx):
	await ctx.send("Horas de trabajo:\nhttps://docs.google.com/spreadsheets/d/13j8lxdUCMzTudtC3HGGWtAoeJ6iOhrUHH2DQiwYrKLU/edit?usp=sharing")

client.run(token)
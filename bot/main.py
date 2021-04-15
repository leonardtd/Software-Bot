import discord 
from discord.ext import commands
import os
from dotenv import load_dotenv
#Task Management
from tasks import *

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

#Comandos para manejo de tareas tasks.py
@client.command()
async def add(ctx, *args):
	task = createTaskSentence(args)
	msg = addTask(task)
	await ctx.send(msg)

@client.command()
async def delete(ctx, index):
	msg = deleteTask(int(index))
	await ctx.send(msg)

@client.command()
async def clear(ctx):
	msg = clearTasks()
	await ctx.send(msg)

@client.command()
async def tasks(ctx):
	msg = listAllTasks()
	await ctx.send(msg)

client.run(token)
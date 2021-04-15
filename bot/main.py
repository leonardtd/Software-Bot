import discord 
from discord.ext import commands
import os
from dotenv import load_dotenv
#Task Management
from tasks import *
#FFmpeg
from discord import FFmpegPCMAudio

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

#Comandos de audio
@client.command()
async def audio(ctx):

	voice = ctx.guild.voice_client
	if not voice and ctx.author.voice: #not connected to voice channel
		channel = ctx.message.author.voice.channel
		voice = await channel.connect()
	elif not ctx.author.voice:
		await ctx.send("Debes estar en un canal de voz!")

	source = FFmpegPCMAudio('../audio_files/test.wav')
	player = voice.play(source)

@client.command()
async def oniichan(ctx):

	voice = ctx.guild.voice_client
	if not voice and ctx.author.voice: #not connected to voice channel
		channel = ctx.message.author.voice.channel
		voice = await channel.connect()
	elif not ctx.author.voice:
		await ctx.send("Debes estar en un canal de voz!")

	source = FFmpegPCMAudio('../audio_files/oniichan.wav')
	player = voice.play(source)

@client.command()
async def cabrotu(ctx):

	voice = ctx.guild.voice_client
	if not voice and ctx.author.voice: #not connected to voice channel
		channel = ctx.message.author.voice.channel
		voice = await channel.connect()
	elif not ctx.author.voice:
		await ctx.send("Debes estar en un canal de voz!")

	source = FFmpegPCMAudio('../audio_files/cabrotu.wav')
	player = voice.play(source)

client.run(token)
# LifeBerry

import discord
import os
import lifebot
import server

client = discord.Client()

@client.event
async def on_ready():
	print(f"{client.user} is ready!")
	await client.change_presence(activity=discord.Game("A Game of Life"))
	server.super_run()

@client.event
async def on_message(ctx):
	await lifebot.message(ctx)

try:
	token = os.getenv('token')
	client.run(token)
except Exception as error:
	print(error)


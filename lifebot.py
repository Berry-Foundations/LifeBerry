# Life Bot

import discord
import asyncio
import random

lifecount = {}

async def message(ctx):
	channel = ctx.channel

	channel_file = open("channel.csv", 'r')
	channel_list = channel_file.read().split(",")
	channel_file.close()

	if str(channel.id) in channel_list:
		pass
	else:
		return

	if channel.id in lifecount:
		lifecount[channel.id] += 1
	else:
		lifecount.update(
			{
				channel.id : 0
			}
		)
	
	count = lifecount[channel.id]

	await asyncio.sleep(5 * 60)

	if str(channel.id) in channel_list:
		pass
	else:
		return

	alive_text = [
		"This chat isn't dead.",
		"I'm still awake...",
		"I'm waiting for someone to chat!!!",
		"I hope I'm not alone.",
		"Hmmmmmmmmmm...",
		"I like to talk!",
		"Till I'm here the heart of the server will still beat!",
		"Wow! That's an unusual silence..."
	]

	if count == lifecount[channel.id]:
		try:
			await ctx.channel.send(alive_text[random.randint(0, len(alive_text) - 1)])
		except Exception as error:
			print(error)

async def add_channel(ctx):
	channel_file = open("channel.csv", 'r')
	channel_list = channel_file.read().split(",")
	channel_file.close()

	embed = discord.Embed(
		title = "**LifeBerry**",
		description = "*Let there be Life...*",
		color = 0xff5757
	)
	embed.set_thumbnail(url=ctx.guild.me.avatar_url)
	embed.set_footer(
		text = "Services under Berry Foundations - Attachment Studios",
		icon_url = "https://images-ext-1.discordapp.net/external/x_dF_ppBthHmRPQi75iuRXLMfK0wuAW2sBLTdtNlXAc/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/894098855220617216/d9b9a3b48a054b9847401bb9178ed438.webp"
	)

	if str(ctx.channel.id) in channel_list:
		pass
	else:
		if ctx.channel.type == discord.ChannelType.private:
			pass
		else:
			channel_file = open("channel.csv", 'a')
			channel_list = channel_file.write(f",{ctx.channel.id},")
			channel_file.close()


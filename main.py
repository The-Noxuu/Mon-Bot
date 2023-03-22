import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "s!", description = "Bot by The Noxuu", intents = intents)

@bot.event
async def on_ready():
	print("Ready !")

bot.run("MTA4ODE3MDk2ODE2NzQ4MTQ5NA.GyJJzp.2zugL4I7JxSQRhKj7Gb-Vf3pLGu7pJUPXaHvp8")
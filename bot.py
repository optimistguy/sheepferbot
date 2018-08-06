import discord
from discord.ext import commands

TOKEN = ''

client = commands.Bot(command_prefix = './CST')

@client.event
async def on_ready():
    print('Bot is ready.')

client.run(process.env.BOT_TOKEN)

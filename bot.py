import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

TOKEN = 'NDc1OTcxNzYwMjkxMDUzNTY5.Dkm_lw.MZr8uiHf4Pl6LoLQy8YiUfyAQKo'

client = commands.Bot(command_prefix = 's!', case_insensitive=False)
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='SomethingElse'))
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Servants 🌾')
    await client.add.roles(member, role)
    await client.say('Hi ' + member + '. ' + 'Wellcome to this community')

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@client.event
async def on_reaction_remove(reaction, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('.hack'):
        msg = 'I am just a sheepfer {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def pong():
    await client.say('There are no game called Pong Ping in my library :(')

@client.command()
async def help():
    await client.say('Sending some help')
    await client.say('Wait')
    await client.say('@Josh ¯\_(ツ)_/¯#1102 still working on it')

@client.command()
async def hack():
    msg = 'I am just a sheepfer {0.author.mention}'.format(msg)
    await client.send_message(message.channel, msg)

@client.command()
async def img():
    msg = 'I am just a sheepfer {0.author.mention}'.format(msg)
    await client.send_message(message.channel, msg)




client.run(TOKEN)

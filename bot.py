import discord
from discord.ext import commands

TOKEN = 'SomethingElse'

client = commands.Bot(command_prefix = '.', case_insensitive=False)
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


@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def pong():
    await client.say('There are no game called Pong Ping in my library :(')

@client.command()
async def help():
    await client.say('Sending some help')
    sleep(2)
    await client.say('Wait')
    sleep(1)
    await client.say('@Josh ¯\_(ツ)_/¯#1102 still working on it')


client.run(TOKEN)

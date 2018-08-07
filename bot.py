import discord
from discord.ext import commands
from random import randint


TOKEN = 'YourTokenHere!'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='SomethingElse'))
    print('Bot is ready.')

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@client.event
async def on_reaction_remove(reaction, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))


@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def pong():
    await client.say('There are no game called Pong Ping in my library :(')



@client.command()
async def flitcoin():
    choice = randint(1,2)
    if choice == 1:
        msg = 'Tail {0.author.mention}'.format(msg)
        await client.send_message(message.channel, msg)
    if choice == 2:
        msg = 'Head {0.author.mention}'.format(msg)
        await client.send_message(message.channel, msg)




client.run(TOKEN)

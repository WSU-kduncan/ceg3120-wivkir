import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    DnD_quotes = [
        'Barbosa: Im going to bed',
        'Aloe: I cast magic missile',
        'Blonic: Im gonna feed Robert a carrot',
        'Calypso: This is my boat now, you can work for me',
        'Zephyr: Right, this looks bad, but Ive got a great explanation',
        'Grover: Ill use my hwip',
        'Azariah: I think Ill cast Flame Blade',
        'Fresh Prince: I know I was locked in a dungeon, but you guys can totally trust me',
        'Fafnir: *explodes*',
        'Eldan: Everyone listen up, Ive got a plan',
    ]

    if "Jeremead" in message.content:
        response = random.choice(DnD_quotes)
        await message.channel.send(response)

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

client.run(TOKEN)

# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name ==GUILD, client.guilds)
    #guild = discord.utils.get(client.guilds,name=GUILD)
    
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Member:\n - {members}')
    
@client.event
async def on_member_join(member):
    member.create_dm()
    member.dm_channel_send(f'Hi {member.name}, welcome to {GUILD}!')


@client.event
async def on_message(message):
    #if message.author == client.user:
        #return
        
    book_recommendations = [
        'pls ferret'
        #'yes, yes you do',
        ]
    if message.content == 'pls ferret':
        response = random.choice(book_recommendations)
        await message.channel.send(response)

client.run(TOKEN)
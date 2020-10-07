# bot2.py
import discord
import os
import random
from dotenv import load_dotenv

#1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#2
bot = commands.Bot(command_prefix= '#')

#Message When bot connects to Discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

#@bot.command(name = "rollDice", help = "Use #recommend before each command")
#async def rollDice(ctx, diceCount:int, sideCount:int):
#    result = ""
#    for n in range(diceCount):
#        result += " " + str(random.randint(1, sideCount))
#    await ctx.send(result)
#    
#@bot.command(name = "createChannel")
#@commands.has_role("Admins")
#async def create_channel(ctx, channel_name = "New_Channel"):
#    guild = ctx.guild
#    existing = discord.utils.get(guild.channels, name = channel_name)
#    if not existing:
#      print("Creating a new Channel ", channel_name)
#      await guild.create_text_channel(channel_name)

#Recommends a Book... duh
@bot.command(name = "recommendBook", help = "Recommends a Book")
async def recommendBook(ctx):
    books = [
    "The Martian by Andy Weir",
    "The Trials of Apollo Serires by Rick Riordan",
    "The Kane Chronicles by Rick Riordan",
    "The Percy Jackson Series by Rick Riordan",
    "The Magnus Chase Trilogy by Rick Riordan",
    "The Hereos of Olympus Series by Rick Riordan",
    "Dr. Space Junk vs the Universe by Alice Gorman",
    "Dune by Frank Herbert",
    "The Hitchhikers Guide to the Galaxy by Douglas Adams",
    "Lord of the Flies by William Goulding",
    "Astrophysics for People in a Hurry by Neil DeGrasse Tyson",
    "Cosmos by Carl Sagan",
    "The Spy School Series by Stuart Gibbs",
    "The Moon Base Alpha Series by Stuart Gibbs",
    "Artemis by Andy Weir",
    "The Hunger Hunger Games Trilogy by Suzanne Collins",
    "Packing for Mars by Mary Roach"
    ]
    book = random.choice(books)
    await ctx.send(book)

#Recommends a Movie... duh
@bot.command(name = "recommendMovie", help = "Recommends a Movie")
async def recommendMovie(ctx):
    movies = [
    "The Martian",
    "Ace Ventura: Pet Detective"
    ]
    movie = random.choice(movies)
    await ctx.send(movie)

#Recoomends a Show... I think you're starting to get it now
@bot.command(name = "recommendShow", help = "Recommends a Show")
async def recommendShow(ctx):
    shows = [
    "The Grand Tour",
    "Top Gear (the original)"
    ]
    show = random.choice(shows)
    await ctx.send(show)

bot.run(TOKEN)


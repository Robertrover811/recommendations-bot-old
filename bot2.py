from flask import Flask
import discord
import os
from threading import Thread
import random
from dotenv import load_dotenv
from discord.ext import commands
import requests
from bs4 import BeautifulSoup as bs

# ---------------------- URLs --------------------------

URL = "https://www.amazon.com/charts"

# --------------------- CLASSES ------------------------

class Book:
  def Book(self):
    self.Title = ''
    self.Author = ''
    self.Publisher = '' 
    self.list_duration = '' 
    self.reviews = ''
  
  def __str__(self):
    return f"Title: {self.Title} : Author: {self.Author}\n"

  def __repr__(self):
    return self.__str__()

# Initializations
app = Flask('')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix= '$')
bot.remove_command('help')

# Embeds
@bot.command(name = "sendEmbed")
async def sendEmbed(ctx):
	embedVar = discord.Embed(title="tanks", description="boats", color=0x000053)
	await ctx.send(embed=embedVar)

# ------------------ Discord bot method definitions------------------

#Message When bot connects to Discord
@bot.event
async def on_ready():
	  # Change status of bot
    await bot.change_presence(activity=discord.Game('My Prefix is $'))
    print(f'{bot.user.name} has connected to Discord!')

# rollDice feature - not really useful for the purpose of the bot...

# @bot.command(name = "rollDice", help = "Use #recommend before each command")
# async def rollDice(ctx, diceCount:int, sideCount:int):
#    result = ""
#    for n in range(diceCount):
#        result += " " + str(random.randint(1, sideCount))
#    await ctx.send(result)

# createChannel - maybe i'll put it back in

# @bot.command(name = "createChannel", help = "Creates a channel with your requested name")
# @commands.has_role("Admins")
# async def create_channel(ctx, channel_name = "New_Channel"):
#    guild = ctx.guild
#    existing = discord.utils.get(guild.channels, name = channel_name)
#    if not existing:
#      print("Creating a new Channel ", channel_name)
#      await guild.create_text_channel(channel_name)

#help Menu 

@bot.command(name = "help", help = "Shows this menu")
async def commands(ctx):
  commands = [
    "**$recommendBook**: Recommends a book to you", "**$recommendMovie**: Recommends a movie to you", "**$recommendShow**: Recommends a Show to you","**$vizz**: Informs you what Recommendations Bot thinks of his best friend, Vizz!","**$help**: Displays this menu"
  ]
  finalString = "" # append to this string
  for i in commands: # concats all the array elements into one string
    finalString += i + "\n"
  embedVar = discord.Embed(title="Help Menu", description=finalString, color=0x000053)
  await ctx.send(embed=embedVar)


#Recommends a Book... duh
@bot.command(name = "recommendBook")
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
    "The Hunger Games Trilogy by Suzanne Collins",
    "Packing for Mars by Mary Roach",
    "Keeper of the Lost Cities Series by Shannon Messenger"
    ]
    book = random.choice(books)
#it works when its commented so dont uncomment... i dont know why
    # output = ""
    # for book in books:
    #    output += book.__str__()
    # await ctx.send(output)
    # await ctx.send(book)
    embedVar = discord.Embed(title="Your book", description=book, color=0x000053)
    await ctx.send(embed=embedVar)

@bot.command(name = "amazonRecommend")
async def amazonRecommend(ctx):
  page = requests.get(URL)
  soup = bs(page.content,'html.parser')

  entries = []
  for i in range(20):
    temp = soup.find('div',id=f"rank{i+1}")
    entries.append(temp)

  books = []
  for entry in entries:
    temp = Book()
    temp.Title = entry.find('div',class_="kc-rank-card-title").text
    temp.Author = entry.find('div',class_="kc-rank-card-author").text
    temp.Publisher = entry.find('div',class_="kc-rank-card-publisher").text
    # temp.list_duration = entry.find('div',class_="kc-wol").text
    temp.reviews = entry.find('div',class_="numeric-star-data").text
    books.append(temp)
  # build the appropriate response from book strings
  output = ""
  for i in range(len(books)):
    output += f"#{i+1})\n"
    output += books[i].__str__()
    output += "\n\n"
  await ctx.send(output)

def stringFormat(books):
  pass

#Recommends a Movie... duh
@bot.command(name = "recommendMovie")
async def recommendMovie(ctx):
    movies = [
    "The Martian",
    "Ace Ventura: Pet Detective"
    ]
    movie = random.choice(movies)
    embedVar = discord.Embed(title="Your book", description=movie, color=0x000053)
    await ctx.send(embed=embedVar)

#Recoomends a Show... I think you're starting to get it now
@bot.command(name = "recommendShow")
async def recommendShow(ctx):
    shows = [
    "The Grand Tour",
    "Top Gear (the original)"
    ]
    show = random.choice(shows)
    embedVar = discord.Embed(title="Your Show", description=show, color=0x000053)
    await ctx.send(embed=embedVar)

#Recommendations Bots Best Friend, Vizz!
@bot.command(name = "vizz")
async def vizz(ctx):
    opinions = [
      "Vizz is my best friend!",
      "Vizz and I are tru friends ",
      "Go check out Vizz, the best moderation/fun bot!"
    ]
    opinion = random.choice(opinions)
    embedVar = discord.Embed(title="Recommendations Bot's Opinions on Vizz", description="Recommendations' Opinion: " + opinion,color=0x000053)
    await ctx.send(embed=embedVar)

@bot.command(name = "logout", help = "Just for debugging")
async def restartBot(ctx):
		await ctx.send("test")
    # await ctx.bot.logout()
    # await login("your_token", bot=True)
    

# -------------------- Flask method definitions ------------------------

@app.route('/', methods=["GET"])
def home():
	return "Recommendations bot has connected to Discord!"
def run():
	app.run(host='0.0.0.0',port=8080)

if __name__ == "__main__":
  t = Thread(target=run)
  t.start()
  bot.run(TOKEN)

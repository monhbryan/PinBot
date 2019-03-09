#ZomBry
from discord.ext import commands
import discord
import asyncio

bot = commands.Bot(
    command_prefix="!",
    status=discord.Status.idle,
    game=discord.Game(name="Booting...")
    )

@bot.event
async def on_ready():
    print("Ready to go!")
    print("Serving: {len(bot.guilds)} guilds.*")

    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')
    await bot.change_presence(status=discord.Status.online, game=discord.Game(name="Active!"))

@bot.command(description="What do you think?")
async def ping():
    await bot.say("Pong")

@bot.command(description="Adds two numbers together")
async def add(left : int=0, right : int=0):
    await bot.say(left + right)

# GLOBAL VARIABLE TO HOLD PINNED MSGS - TO BE CHANGED    
PinnedMsg = {}
#
@bot.command(description="Creates a pin")
async def createPin(messageKey, message):
    PinnedMsg[str(messageKey)] = message
    await bot.say("Pinned message created successfully")
@bot.command(description="Removes a pin")
async def removePin(messageKey):
    del PinnedMsg[messageKey]
    await bot.say("Pinned message deleted successfully")
    
@bot.command(description="Lists all pins")
async def listPin():
    await bot.say("Number of Pinned Items :"+str(len(PinnedMsg)))
    await bot.say(str(PinnedMsg))

@bot.command(description="Shows a pinned message")
async def pin(messageKey):
    await bot.say(str(PinnedMsg[messageKey]))

#Bot token - Hidden for obv reasons
from token1 import token
bot.run(token)

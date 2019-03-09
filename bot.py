#ZomBry
from discord.ext import commands
import discord
import asyncio
import sqlitedict

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

@bot.command(description = "Changes the prefix of commands")
async def prefix(PreFix):
    bot.command_prefix=PreFix[0]
    await bot.say("Prefix changed to: " + PreFix[0])

@bot.command(description="What do you think?")
async def ping():
    await bot.say("Pong")

# DATABASE FOR PINS
from sqlitedict import SqliteDict
PinnedMsg = SqliteDict('./my_db.sqlite', autocommit=True)
#

@bot.command(description="Creates a pin")
async def createp(messageKey, message):
    PinnedMsg[str(messageKey)] = message
    await bot.say("Pinned message created successfully")
    
        
@bot.command(description="Removes a pin")
async def removep(messageKey):
    del PinnedMsg[messageKey]
    await bot.say("Pinned message deleted successfully")
    
@bot.command(description="Lists all pins")
async def listp():
    await bot.say("Number of Pinned Items : " + str(len(PinnedMsg)))
    for key, value in PinnedMsg.iteritems():
        if len(value) < 100:
            await bot.say(key + ' = ' + value)
        else:
            await bot.say(key + ' = ' + value[0:100] + '...')

@bot.command(description="Shows a pinned message")
async def pin(messageKey):
    await bot.say(str(PinnedMsg[messageKey]))



#Bot token - Hidden for obv reasons
from token1 import token
bot.run(token)

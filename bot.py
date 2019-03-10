#ZomBry
from discord.ext import commands
import discord
import asyncio
import sqlitedict
command_prefix = "!"
bot = commands.Bot(
    command_prefix="!",
    status=discord.Status.idle,
    game=discord.Game(name="Booting...")
    )

@bot.event
async def on_ready():
    print("Ready to go!")
    print("Serving: "+str(len(bot.servers))+ " guilds.")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')
    await bot.change_presence(status=discord.Status.online, game=discord.Game(name="Active!"))

@bot.command(description="What do you think?")
async def ping():
    await bot.say("Pong")

# DATABASE FOR PINS
from sqlitedict import SqliteDict
PinnedMsg = SqliteDict()
#
def helperMessage(message, command):
        return message.content.replace(command_prefix+command+" ", "")
@bot.event
async def on_message(message):
    global PinnedMsg
    PinnedMsg= SqliteDict('./Servers/'+str(message.server.id)+'.sqlite', autocommit=True)
    if message.author == bot.user:
        return
    if message.content.startswith(command_prefix+"createp"):
        await createp(message)
    elif message.content.startswith(command_prefix+"removep"):
        await removep(message)
    elif message.content.startswith(command_prefix+"listp"):
        await listp(message)
    elif message.content.startswith(command_prefix+"pin"):
        await pin(message)
    elif message.content.startswith(command_prefix+"prefix"):
        await prefix(message)
    

async def createp(message):
    fullMess = helperMessage(message,"createp")
    messList = fullMess.split(" ",1)
    PinnedMsg[messList[0]] = messList[1]
    await bot.send_message(message.channel,"Pinned message created successfully")

async def removep(message):
    fullMess = helperMessage(message,"removep")
    del PinnedMsg[fullMess]
    await bot.send_message(message.channel,"Pinned message deleted successfully")

async def listp(message):
    fullMess = helperMessage(message,"listp")
    await bot.send_message(message.channel,"Number of Pinned Items : " + str(len(PinnedMsg)))
    for key, value in PinnedMsg.iteritems():
        if len(value) < 100:
            await bot.send_message(message.channel,key + ' = ' + value)
        else:
            await bot.send_message(message.channel,key + ' = ' + value[0:100] + '...')
            
async def pin(message):
    fullMess = helperMessage(message,"pin")
    await bot.send_message(message.channel,str(PinnedMsg[fullMess]))
    
async def prefix(message):
    fullMess = helperMessage(message,"prefix")
    global command_prefix
    command_prefix = fullMess[0]
    await bot.send_message(message.channel,"Prefix changed to: " + command_prefix)

#Bot token - Hidden for obv reasons
from token1 import token
bot.run(token)

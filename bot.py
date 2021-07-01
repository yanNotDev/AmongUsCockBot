import discord, random
from discord.ext import commands

from dotenv import load_dotenv
from os import getenv
load_dotenv()

token = getenv("TOKEN")

from cocks import cocks

bot = commands.Bot(command_prefix="")


@bot.event
async def on_ready():
    print("sussy")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="ping for among us cock"))

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send( "```\n" + random.choice(cocks) + "\n```" )

bot.run(token)

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix='>')
token = os.getenv("TOKEN")


@bot.event
async def on_ready():
    print("AmongBot 2.0 is ready.")


@bot.command()
async def load(ctx, extension):
    try:
        bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded **{extension}**.")
    except Exception as err:
        await ctx.send(f"Couldn't unload **{extension}**. Error: *{str(err)}*")


@bot.command()
async def unload(ctx, extension):
    try:
        bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"Unloaded **{extension}**.")
    except Exception as err:
        await ctx.send(f"Couldn't unload **{extension}**. Error: *{str(err)}*")


@bot.command()
async def reload(ctx, extension):
    try:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Reloaded **{extension}**.')
    except Exception as err:
        await ctx.send(f"Couldn't reload **{extension}**. Error: *{str(err)}*")

for fileName in os.listdir("./cogs"):
    if fileName.endswith(".py"):
        bot.load_extension(f"cogs.{fileName[:-3]}")

bot.run(token)

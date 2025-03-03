import discord
import os
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Watching(name='Evergreen City Roleplay', url='https://www.twitch.tv/urtwitchusername'))

bot.run('MTI2Mjk2NzQ3NjI0OTk1NjM3Mw.G5w8sZ.iRoWSWFNk3-SBYsseUHD6OGsNAdTz_DQlnVGDo')

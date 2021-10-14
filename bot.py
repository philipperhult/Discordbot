from discord.ext import commands
import discord
import time
import os
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix = '!')

@bot.command(pass_context=True)
async def check(ctx):
    await ctx.send("Ja den funke din dog")

@bot.command(pass_context=True)
async def gåut(ctx, member: discord.Member):

    channelID = member.voice.channel

    channel = discord.utils.get(ctx.guild.voice_channels, name='GÅ UT!')
    channel2 = discord.utils.get(ctx.guild.voice_channels, name=f'{channelID}')

    while True:
        await member.edit(voice_channel=channel)
        await member.edit(mute=True)
        time.sleep(20)
        await member.edit(mute=False)
        await member.edit(voice_channel=channel2)
        return False

@bot.command(pass_context=True)
async def test(ctx, role: discord.Role):
    user = ctx.message.author
    await user.add_roles(role)

bot.run(os.environ.get('RUNTOKEN'))


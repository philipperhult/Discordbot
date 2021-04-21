from discord.ext import commands
import discord
import os
import time

bot = commands.Bot(command_prefix = '$')

@bot.command(pass_context=True)
async def check(ctx):
    await ctx.send("Ja den funke, nå gå ut")

@bot.command(pass_context=True)
async def gåut(ctx, member: discord.Member):

    #channelID = member.voice_channel.id

    channel = discord.utils.get(ctx.guild.voice_channels, name='GÅ UT!')
    channel2 = discord.utils.get(ctx.guild.voice_channels, name='Lounge')

    while True:
        await member.edit(voice_channel=channel)
        await member.edit(mute=True)
        time.sleep(20)
        await member.edit(mute=False)
        await member.edit(voice_channel=channel2)
        return False
    

bot.run("NzcwMjg1NTU0MTkyNjEzNDE2.X5bWUw.oRXxJus_Q8hMJWeLr_cjfxmkt-k")



#https://discord.com/api/oauth2/authorize?client_id=770285554192613416&permissions=29427712&scope=bot